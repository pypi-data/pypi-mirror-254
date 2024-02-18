import cv2

def resize_pad(frame, new_shape=(640, 640)):
    ori_width, ori_height = frame.shape[:2][::-1]
    new_width, new_height = new_shape # 宽 高

    resize_rate = min(new_width / ori_width, new_height / ori_height)

    out_width = int(ori_width * resize_rate)
    out_height = int(ori_height * resize_rate)

    x_shift = (new_width - out_width) // 2
    y_shift = (new_height - out_height) // 2

    resized = cv2.resize(frame, (out_width, out_height))
    resized_padded = cv2.copyMakeBorder(resized, y_shift, y_shift, x_shift, x_shift, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    roi = [[x_shift, y_shift], [x_shift + out_width, y_shift + out_height]]

    return resized_padded, roi

def matting(frame, roi):
    (x0, y0), (x1, y1) = roi
    frame = frame[y0:y1, x0:x1]
    return frame

