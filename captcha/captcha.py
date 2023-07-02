import base64
import io
import os
import re

import cv2
import numpy as np
import pytesseract
import requests
from PIL import Image


def decode_captcha(image: Image) -> str:
    if os.name == "nt":
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    image = np.array(image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.blur(image, (4, 4))
    image = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(image)
    text = re.sub(r"[^A-Z]*", "", text)
    return text


def decode_captcha_url(url: str) -> str:
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    return decode_captcha(image)


def decode_captcha_base64(img_base64: str, save_filename: str = None) -> str:
    base64_split = img_base64.split("base64,")
    imgdata = base64.b64decode(base64_split[-1].strip())
    image = Image.open(io.BytesIO(imgdata))

    if save_filename is not None:
        image.save(save_filename)

    return decode_captcha(image)
