from io import BytesIO
from PIL import Image
import cv2
import numpy as np
import base64

def cv2_image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

def cv2_to_pil(cv2_img):
    if not cv2:
        raise ImportError("OpenCv was never found during boot. Install opencv to use this function")
    return Image.fromarray(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))

def pil_to_cv2(pil_img):
    if not cv2:
        raise ImportError("OpenCv was never found during boot. Install opencv to use this function")
    if not Image:
        raise ImportError("PIL was never found during boot. Install Python Image Lib. to use this function")
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

def pil_to_memory_file(pil_img, format="JPEG"):
    if BytesIO == False:
        raise ImportError("BytesIO was never found, please install it to use this feature")
    img_io = BytesIO()
    pil_img.save(img_io, format)
    img_io.seek(0)
    return img_io

def base64_to_pil(base64_str=None, base64_bytes=None):
    if not base64:
        raise ImportError("Base64 was never found, please install it to use this feature")
    img_io = BytesIO()
    if base64_str is not None:
        img_io.write(base64.decodebytes(base64_str.encode()))
    else:
        img_io.write(base64.decodebytes(base64_bytes))
    img_io.seek(0)
    pil_img = Image.open(img_io)
    return pil_img

def pil_to_base64(pil_image, format="JPEG"):
    buffered = BytesIO()
    pil_image.save(buffered, format=format)
    buffered.seek(0)
    return base64.b64encode(buffered.getvalue())

def cv2_convert_to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)