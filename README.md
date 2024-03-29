# Captcha

## Description

![Captcha image](https://raw.githubusercontent.com/neati/captcha/main/captcha.jpg)

Analyze the captcha using OpenCV and Tesseract.

## Requirements

### Tesseract

**macOS**

```bash
brew install tesseract
```

**Windows**

https://github.com/UB-Mannheim/tesseract/wiki

## Install

```bash
pip install git+https://github.com/neati/captcha.git
```

## Usage

```python
from captcha import decode_captcha_url

str = decode_captcha_url("https://raw.githubusercontent.com/neati/captcha/main/captcha.jpg")
```

```python
from captcha import decode_captcha_base64

captcha_base64 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD..."
str = decode_captcha_base64(captcha_base64)
```
