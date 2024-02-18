"""hekaiyue 何恺悦 2024-01-26"""
import cv2
import numpy
import base64

def cv_b64(frame_cv):
    frame_b64 = str(base64.b64encode(cv2.imencode(".jpg", frame_cv)[1]))[2:-1]
    return frame_b64

def b64_cv(frame_b64):
    frame_cv = cv2.imdecode(numpy.frombuffer(base64.b64decode(frame_b64), numpy.uint8), cv2.IMREAD_COLOR)
    return frame_cv

def b_b64(file_b):
    file_b64 = base64.b64encode(file_b).decode("utf-8")
    return file_b64

def b64_b(file_b64):
    file_b = base64.b64decode(file_b64)
    return file_b
