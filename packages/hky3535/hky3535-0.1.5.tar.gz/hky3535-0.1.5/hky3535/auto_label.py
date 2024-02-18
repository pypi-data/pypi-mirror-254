"""hekaiyue 何恺悦 2024-01-29"""
from . import b64
from tqdm import tqdm # python3 -m pip install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple
import cv2
import os
import requests
from pathlib import Path
import xml.etree.ElementTree as ET

def init(base_url, weight_path, config_path):
    # 查看模型是否已经被加载
    response = requests.post(url=f"{base_url}/status", json={})
    if "hky3535" in response.json()["response"]["grounding_dino"]: return {}
    # 如果没有被加载则上传模型并加载
    data = {
        "engine_name": "grounding_dino", 
        "engine_task": "hky3535", 
        "arguments": {
            "weight": {"name": Path(weight_path).name, "b64": b64.b_b64(open(weight_path, "rb").read())},
            "config": {"name": Path(config_path).name, "b64": b64.b_b64(open(config_path, "rb").read())}, 
            "device": "gpu"
        }
    }
    response = requests.post(url=f"{base_url}/load", json=data)
    return response.json()

def run(base_url, storage_path, classes, conf=0.25, iou=0.7):
    def infer(frame, conf, iou, classes):
        # classes中有多个合并项 将所有合并项进行提前合并并记录下index
        classes_map = [class_key for class_key in classes for class_value in classes[class_key]]
        classes = [class_value for class_key in classes for class_value in classes[class_key]]
        data = {
            "engine_name": "grounding_dino", 
            "engine_task": "hky3535", 
            "arguments": {
                "frame": {"b64": b64.cv_b64(frame)}, 
                "conf": conf, "iou": iou, 
                "text_prompt": classes, "text_threshold": conf
            }
        }
        response = requests.post(url=f"{base_url}/infer", json=data)
        results = response.json()["response"] # 得到推理结果
        for result in results: result[5] = classes_map[result[5]] # 映射得到最终的标签
        # [[x0, y0, x1, y1, conf, class_name], ...]
        return results
    
    def save_xml(storage_path, file_stem, width, height, results):
        # 递归转换：dict --> xml
        def dict2xml(element, data):
            for key, value in data.items():
                if isinstance(value, dict):
                    sub_element = ET.SubElement(element, key)
                    dict2xml(sub_element, value)
                elif isinstance(value, list):
                    for _item in value:
                        sub_element = ET.SubElement(element, "object")
                        dict2xml(sub_element, _item)
                else:
                    sub_element = ET.SubElement(element, key)
                    sub_element.text = str(value)

        # 整理出识别结果对应的基础dict结构
        results = {
            "filename": f"{file_stem}.jpg", 
            "size": {"width": width, "height": height, "depth": 3}, 
            "segmented": 0, 
            "object": [{
                "name": class_name, 
                "pose": "Unspecified", 
                "truncated": 0, 
                "difficult": 0, 
                "bndbox": {"xmin": x0, "ymin": y0, "xmax": x1, "ymax": y1,}
            } for x0, y0, x1, y1, conf, class_name in results]
        }
        
        # 新建一个xml结构 并写入dict转换出来的xml并保存至本地
        root = ET.Element("annotation")
        dict2xml(root, results)
        ET.ElementTree(root).write(f"{storage_path}/{file_stem}.xml", encoding="utf-8", xml_declaration=True)
    
    # 仅接受jpg+xml的格式
    files_name = os.listdir(storage_path)
    # 检查是否有非jpg或者xml的文件
    for file_name in files_name:
        if not file_name.endswith((".jpg", ".xml")):
            print(f"程序仅接受.jpg和.xml文件！{file_name}")
            return 
    # 获取到所有文件名（去除后缀后的文件名）
    files_stem = list(set([Path(file_name).stem for file_name in files_name]))
    
    # 主循环：逐个遍历图像
    for file_stem in tqdm(files_stem, total=len(files_stem)):
        # 如果对应xml已存在则不进行预标注
        if f"{file_stem}.xml" in files_name: continue
        # 读取一张图像
        frame = cv2.imread(f"{storage_path}/{file_stem}.jpg")
        width, height = frame.shape[:2]
        # 推理得到目标检测结果
        results = infer(frame=frame, conf=conf, iou=iou, classes=classes)
        # 整理结果并存入xml中
        save_xml(
            storage_path=storage_path, 
            file_stem=file_stem, 
            width=width, 
            height=height, 
            results=results
        )
