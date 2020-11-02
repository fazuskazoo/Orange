import pathlib
from setuptools import setup, parse_requirements

here = pathlib.Path(__file__).parent

install_reqs = parse_requirments('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]
print(reqs)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
 name="oxrange",
 version="0.0.3",
 author="Fazus Kazoo",
 description="Python things",
 long_description=long_description,
 long_description_content_type="text/markdown",
 license="GPL",
 url="https://github.com/fazuskazoo/Orange",
 packages=["orange"],
 python_requires='>=3.8',
 include_package_data=True,
 install_requires=reqs,
 classifiers=[
  "Programming Language :: Python :: 3",
  "Operating System :: POSIX :: Linux",
 ],
 entry_points={
      "console_scripts": [
           ]
     }
)
