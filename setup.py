import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent

setup(
 name="orange",
 version="0.0.1",
 author="Fazus Kazoo",
 descriptiong="Python things",
 license="GPL",
 url="https://github/fazuskazoo.com/Orangei",
 packages=["orange"],
 include_package_data=True,
 entry_points={
      "console_scripts": [

           ]
     }
)
