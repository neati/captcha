from setuptools import setup

setup(
    name="captcha",
    version="0.0.1",
    description="Decode captcha images",
    url="https://github.com/neati/captcha.git",
    author="neati",
    author_email="p@neati.com",
    packages=["captcha"],
    install_requires=["numpy", "opencv-python", "pytesseract"],
)
