import base64
import io
import os
import re

import cv2
import numpy as np
import pytesseract
from PIL import Image


def decode_captcha(img_base64: str, filename: str = None) -> str:
    if os.name == "nt":
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    base64_split = img_base64.split("base64,")
    imgdata = base64.b64decode(base64_split[-1].strip())

    pil_image = Image.open(io.BytesIO(imgdata))
    image = np.array(pil_image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.blur(image, (4, 4))
    image = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(image)
    text = re.sub(r"[^A-Z]*", "", text)

    if filename is not None:
        pil_image.save(filename)

    return text
