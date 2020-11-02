import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
 name="orange",
 version="0.0.1",
 author="Fazus Kazoo",
 description="Python things",
 long_description=long_description,
 long_description_content_type="text/markdown",
 license="GPL",
 url="https://github/fazuskazoo.com/Orange",
 packages=["orange"],
 python_requires='>=3.8',
 include_package_data=True,
 entry_points={
      "console_scripts": [
           ]
     }
)
