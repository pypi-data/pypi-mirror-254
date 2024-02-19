from setuptools import setup
import pathlib

path = pathlib.Path(__file__).parent.resolve()
readmetxt = (path/"README.rst").read_text()

setup(name="chengyiLib",
      version="1.0.0",
      description="this is a chengyi test .py file",
      packages=["chengyiLib","chengyiLib2"],
      py_modules=["Tool","Tool2"],
      author="spiderMan_007",
      author_email="17888841257@163.com",
      long_description=readmetxt)