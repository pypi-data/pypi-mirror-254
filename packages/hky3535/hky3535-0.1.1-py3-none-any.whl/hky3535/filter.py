"""hekaiyue 何恺悦 2024-01-26"""
from datetime import datetime
import cv2
import numpy

def in_period(periods=[]):
    # [["06:00", "08:00"], ...] --> [[<datetime>, <datetime>], ...]
    periods = [list(map(lambda x: datetime.strptime(x, "%H:%M").time(), period)) for period in periods] if len(periods) > 0 else True
    # 如果检测时间为空则默认任何时间都在检测时间内
    if periods is True: return True
    # 比对当前时间在哪个区间内，返回所在的第一个时间区间
    now = datetime.now().time()
    for index, (period_start, period_end) in enumerate(periods):
        if period_start <= now <= period_end:
            return index
    return False

def in_region(point, regions):
    # [x, y] [[[x0, y0], [x1, y1], [x2, y2], ...], ...]
    for index, region in enumerate(regions):
        if cv2.pointPolygonTest(numpy.array(region), point, False) >= 0: 
            return index
    return False
