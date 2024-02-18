"""hekaiyue 何恺悦 2024-01-26"""
import os 
from setuptools import setup, find_packages

setup(
	name = "hky3535",
	version = "0.1.2",
    author ="hky3535",
    author_email = "hky3535@163.com",
	url = 'https://github.com/hky3535/hky3535.git',
    long_description_content_type="text/markdown",
	long_description = open('README.md',encoding="utf-8").read(),
    install_requires=[
        "opencv-python", 
        "numpy", 
        "pillow", 
        "tqdm", 
        "requests"
    ], 
	packages = find_packages(),
 	license = 'Apache',
   	classifiers = [
       'License :: OSI Approved :: Apache Software License'
    ],
    package_data={'': ['*.ttf']}, 
    include_package_data=True
)
