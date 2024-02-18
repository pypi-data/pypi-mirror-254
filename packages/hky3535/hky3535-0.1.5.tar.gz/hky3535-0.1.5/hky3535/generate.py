import numpy
import random
import mss
import cv2
import numpy

def blank_frame(width, height):
    frame = numpy.zeros((height, width, 3), dtype=numpy.uint8)
    return frame

def screen(index):
    sct = mss.mss()
    monitor = sct.monitors[index]
    while True:
        frame = sct.grab(monitor)
        frame = numpy.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        yield frame

def moving_rectangles():
    return

def moving_points():
    return

def blinking_rectangles():
    return

def blinking_points(regions, hot_spots=False):
    return
