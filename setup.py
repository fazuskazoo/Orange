import pathlib
from setuptools import setup
from pkg_resources import parse_requirements
import distutils.command.build as _build

here = pathlib.Path(__file__).parent

with open('requirements.txt') as fp:
    install_reqs = fp.read()

with open('system_requirements.txt') as fp:
    sysinstall_reqs = fp.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

class SystemBuild(_build.build):
    def run(self):
        print("System Build")
        print(sysinstall_reqs)
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
 install_requires=install_reqs,
 classifiers=[
  "Programming Language :: Python :: 3",
  "Operating System :: POSIX :: Linux",
 ],
 entry_points={
      "console_scripts": [
           ]
     },
 cmdclass={'build': SystemBuild
     },
)
