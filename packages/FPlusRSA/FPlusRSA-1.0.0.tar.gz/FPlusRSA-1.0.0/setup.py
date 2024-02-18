import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open("F:/Python/FPlusRSA/README.md", "r",encoding="utf-8") as fh:
  long_description = fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'a small library, you can use it to implement RSA encryption and decryption and other basic methods'

setup(
  name="FPlusRSA",
  version=VERSION,
  author="FPlusStudio",
  author_email="qweasdghjkx@qq.com",
  description=DESCRIPTION,
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=find_packages(),
  install_requires = [],
  keywords = ["python", "RSA", "encryption algorithm","windows", "mac", "linux"],
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Unix",
  "Operating System :: MacOS :: MacOS X",
  "Operating System :: Microsoft :: Windows"
  ]
)