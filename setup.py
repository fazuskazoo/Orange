import pathlib
from setuptools import setup
from setuptools import Command
from setuptools.command.install import install
from pkg_resources import parse_requirements
from distutils.command.build import build as _build
import setuptools
here = pathlib.Path(__file__).parent
'''
read in data files
'''

with open('requirements.txt') as fp:
    install_reqs = fp.readlines()

with open('system_requirements.txt') as fp:
    sysinstall_reqs = fp.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

'''
    custom build code
'''



"""
https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/complete/juliaset/setup.py

https://github.com/pypa/setuptool

https://www.anomaly.net.au/blog/running-pre-and-post-install-jobs-for-your-python-packages/

"""



setup(
 name="oxrange",
 version="0.0.7",
 author_email="fazuskazoo@gmail.com",
 author="Fazus Kazoo",
 description="Python things",
 long_description_content_type="text/markdown",
 dependency_links=[ "https://pypi.org/simple/" ],
 license="GPL",
 url="https://github.com/fazuskazoo/Orange",
 python_requires='>=3.6',
 include_package_data=True,
 packages=['orange'],
 package_data={
  'orange':['*.json'],

     },
 classifiers=[
  "Programming Language :: Python :: 3",
  "Operating System :: POSIX :: Linux",
 ],
)
