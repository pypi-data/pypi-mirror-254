from shapely.geometry import LineString

def crossed(line0, line1): # 两线段是否相交
    return LineString(line0).intersects(LineString(line1))

def vector(line): # 计算线段的向量
    (x0, y0), (x1, y1) = line
    return [x1-x0, y1-y0]

def clockwise_vector(line): # 计算线段顺时针转90度的向量
    x, y = vector(line)
    return [y, -x]

def acute(vector0, vector1): # 两向量夹角是否锐角
    x0, y0 = vector0
    x1, y1 = vector1
    dot_product = x0*x1 + y0*y1 # 如果点积小于0则判定为锐角 反之为钝角
    return dot_product >= 0

def iou(box0, box1): # 计算两个框的交并比
    # 计算交集的左上角和右下角坐标
    x0 = max(box0[0], box1[0])
    y0 = max(box0[1], box1[1])
    x1 = min(box0[2], box1[2])
    y1 = min(box0[3], box1[3])
    # 计算交集的宽度和高度
    intersection_width = max(0, x1 - x0)
    intersection_height = max(0, y1 - y0)
    # 计算交集面积
    intersection_area = intersection_width * intersection_height
    # 计算并集面积
    box0_area = (box0[2] - box0[0]) * (box0[3] - box0[1])
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    union_area = box0_area + box1_area - intersection_area
    if union_area <= 0: return 0
    # 计算交并比
    iou = intersection_area / union_area
    return iou
