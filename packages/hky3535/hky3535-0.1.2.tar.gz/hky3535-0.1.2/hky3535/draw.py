"""hekaiyue 何恺悦 2024-01-26"""
from os.path import dirname, abspath
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy

def draw_zh(frame, text="默认文字", position=(0, 0), color=(255, 255, 255), font=f"{dirname(abspath(__file__))}/data/MicrosoftYaHei-01.ttf", size=10):
    _frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    _draw = ImageDraw.Draw(_frame)
    _draw.text((position[0], position[1]), text=text, fill=color, font=ImageFont.truetype(font, size))
    frame = cv2.cvtColor(numpy.array(_frame), cv2.COLOR_RGB2BGR)
    return frame
