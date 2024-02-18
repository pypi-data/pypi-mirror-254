# setup.py
from setuptools import setup, find_packages

setup(
    name="qhxc_api",
    version="0.2.2",
    description="An exchange open api SDK",
    packages=find_packages(),
    # py_modules=['openapi.py'],  # 指定要包含的模块或文件
    python_requires='>=3.6'
)