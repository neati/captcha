# Captcha

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
from captcha import decode_captcha

captcha_base64 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD..."
str = decode_captcha(captcha_base64)
```
