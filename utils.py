import base64
import numpy as np
import cv2
import base64

# with open("test.jpg", "rb") as f:
#     im_b64 = base64.b64encode(f.read())

def base64opencv(im_b64):
    im_bytes = base64.b64decode(im_b64)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)

    return img

def opencvbase64(frame):
    retval, buffer = cv2.imencode('.jpg', frame)
    encoded = str(base64.b64encode(buffer))[2:-1]

    return encoded