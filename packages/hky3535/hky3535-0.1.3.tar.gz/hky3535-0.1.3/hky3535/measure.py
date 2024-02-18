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
