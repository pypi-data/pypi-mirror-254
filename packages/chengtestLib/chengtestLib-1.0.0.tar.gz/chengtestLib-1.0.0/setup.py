from distutils.core import setup
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
readme = (here / "README.rst").read_text(encoding="utf-8")

setup(name="chengtestLib",
      version="1.0.0",
      description="this is a testLib",
      packages=["testLib"],
      py_modules=["Tool"],
      author="spiderman",
      author_email="xxx@163.com",
      long_description=readme)