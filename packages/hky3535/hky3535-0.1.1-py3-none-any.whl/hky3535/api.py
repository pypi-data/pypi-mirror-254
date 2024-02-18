import requests
from pathlib import Path
from . import b64

base_url = "" # API部署地址

def post(function, data, timeout):
    try:
        response = requests.post(url=f"{base_url}/{function}", json=data, timeout=timeout)
        if response.status_code != 200: 
            return False, f"请求失败！请求码：{response.status_code}；返回内容：{response.content.decode()}"
        response = response.json() # 解析返回内容 {"ret": True, "response": results}
        return response["ret"], response["response"]
    except Exception as e:
        return False, f"请求崩溃！崩溃原因：{str(e)}"

def status():
    ret, response = post(function="status", data={}, timeout=10)
    if not ret: return False, f"获取状态失败，失败原因：{response}"
    return True, response

def load(data):
    ret, response = post(function="load", data=data, timeout=120)
    if not ret: return False, f"模型加载失败，失败原因：{response}"
    return True, "模型加载成功"

def infer(data):
    ret, response = post(function="infer", data=data, timeout=1)
    if not ret: return False, f"图像推理失败，失败原因：{response}"
    return True, response


class GroundingDino:
    def __init__(self, weight_path, config_path, device="gpu"):
        self.weight_path = weight_path
        self.config_path = config_path
        self.device = device

        self.weight_name = Path(weight_path).name
        self.config_name = Path(config_path).name

        self.engine_name = "grounding_dino"
        self.engine_task = self.weight_name

        self.load() # 加载模型

    def load(self):
        ret, response = status() # 检查模型是否重复加载
        if not ret: return False, response
        if self.engine_task in response[self.engine_name]: return True, "模型已加载，无需重复加载"

        ret, response = load(data={ # 加载模型
            "engine_name": self.engine_name, 
            "engine_task": self.engine_task, 
            "arguments": {
                "weight": {"name": self.weight_name, "b64": b64.b_b64(open(self.weight_path, "rb").read())},
                "config": {"name": self.config_name, "b64": b64.b_b64(open(self.config_path, "rb").read())}, 
                "device": self.device
            }
        })
        return ret, response

    def infer(self, frame, conf=0.25, iou=0.7, text_prompt=False, text_threshold=0.25):
        ret, response = infer(data={
            "engine_name": self.engine_name, 
            "engine_task": self.weight_name, 
            "arguments": {
                "frame": {"b64": b64.cv_b64(frame)}, 
                "conf": conf, "iou": iou, 
                "text_prompt": text_prompt, "text_threshold": text_threshold
            }
        })
        return ret, response


class Yolov4:
    def __init__(self, weight_path, config_path, device="gpu"):
        self.weight_path = weight_path
        self.config_path = config_path
        self.device = device

        self.weight_name = Path(weight_path).name
        self.config_name = Path(config_path).name

        self.engine_name = "yolov4"
        self.engine_task = self.weight_name

        self.load() # 加载模型

    def load(self):
        ret, response = status() # 检查模型是否重复加载
        if not ret: return False, response
        if self.engine_task in response[self.engine_name]: return True, "模型已加载，无需重复加载"

        ret, response = load(data={ # 加载模型
            "engine_name": self.engine_name, 
            "engine_task": self.engine_task, 
            "arguments": {
                "weight": {"name": self.weight_name, "b64": b64.b_b64(open(self.weight_path, "rb").read())},
                "config": {"name": self.config_name, "b64": b64.b_b64(open(self.config_path, "rb").read())}, 
                "device": self.device
            }
        })
        return ret, response

    def infer(self, frame, conf=0.25, iou=0.7, classes=False):
        ret, response = infer(data={
            "engine_name": self.engine_name, 
            "engine_task": self.weight_name, 
            "arguments": {
                "frame": {"b64": b64.cv_b64(frame)}, 
                "conf": conf, "iou": iou, 
                "classes": classes
            }
        })
        return ret, response


class Yolov5:
    def __init__(self, weight_path, device="gpu", half=False):
        self.weight_path = weight_path
        self.device = device
        self.half = half

        self.weight_name = Path(weight_path).name

        self.engine_name = "yolov5"
        self.engine_task = self.weight_name

        self.load() # 加载模型

    def load(self):
        ret, response = status() # 检查模型是否重复加载
        if not ret: return False, response
        if self.engine_task in response[self.engine_name]: return True, "模型已加载，无需重复加载"

        ret, response = load(data={ # 加载模型
            "engine_name": self.engine_name, 
            "engine_task": self.engine_task, 
            "arguments": {
                "weight": {"name": self.weight_name, "b64": b64.b_b64(open(self.weight_path, "rb").read())},
                "device": self.device, 
                "half": self.half
            }
        })
        return ret, response

    def infer(self, frame, conf=0.25, iou=0.7, classes=False):
        ret, response = infer(data={
            "engine_name": self.engine_name, 
            "engine_task": self.weight_name, 
            "arguments": {
                "frame": {"b64": b64.cv_b64(frame)}, 
                "conf": conf, "iou": iou, 
                "classes": classes
            }
        })
        return ret, response


class Yolov5u:
    def __init__(self, weight_path, device="gpu", half=False):
        self.weight_path = weight_path
        self.device = device
        self.half = half

        self.weight_name = Path(weight_path).name

        self.engine_name = "yolov5u"
        self.engine_task = self.weight_name

        self.load() # 加载模型

    def load(self):
        ret, response = status() # 检查模型是否重复加载
        if not ret: return False, response
        if self.engine_task in response[self.engine_name]: return True, "模型已加载，无需重复加载"

        ret, response = load(data={ # 加载模型
            "engine_name": self.engine_name, 
            "engine_task": self.engine_task, 
            "arguments": {
                "weight": {"name": self.weight_name, "b64": b64.b_b64(open(self.weight_path, "rb").read())},
                "device": self.device, 
                "half": self.half
            }
        })
        return ret, response

    def infer(self, frame, conf=0.25, iou=0.7, classes=False):
        ret, response = infer(data={
            "engine_name": self.engine_name, 
            "engine_task": self.weight_name, 
            "arguments": {
                "frame": {"b64": b64.cv_b64(frame)}, 
                "conf": conf, "iou": iou, 
                "classes": classes
            }
        })
        return ret, response


class Yolov8u:
    def __init__(self, weight_path, device="gpu", half=False):
        self.weight_path = weight_path
        self.device = device
        self.half = half

        self.weight_name = Path(weight_path).name

        self.engine_name = "yolov8u"
        self.engine_task = self.weight_name

        self.load() # 加载模型

    def load(self):
        ret, response = status() # 检查模型是否重复加载
        if not ret: return False, response
        if self.engine_task in response[self.engine_name]: return True, "模型已加载，无需重复加载"

        ret, response = load(data={ # 加载模型
            "engine_name": self.engine_name, 
            "engine_task": self.engine_task, 
            "arguments": {
                "weight": {"name": self.weight_name, "b64": b64.b_b64(open(self.weight_path, "rb").read())},
                "device": self.device, 
                "half": self.half
            }
        })
        return ret, response

    def infer(self, frame, conf=0.25, iou=0.7, classes=False):
        ret, response = infer(data={
            "engine_name": self.engine_name, 
            "engine_task": self.weight_name, 
            "arguments": {
                "frame": {"b64": b64.cv_b64(frame)}, 
                "conf": conf, "iou": iou, 
                "classes": classes
            }
        })
        return ret, response

