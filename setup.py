from setuptools import setup

setup(
    name="captcha",
    version="0.0.1",
    description="Decode captcha images",
    url="https://github.com/neati/captcha.git",
    author="neati",
    author_email="p@neati.com",
    packages=["captcha"],
    install_requires=[
        "numpy>=1.25.0",
        "opencv-python>=4.8.0",
        "pytesseract>=0.3.10",
    ],
)
