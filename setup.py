import pathlib
from setuptools import setup
from setuptools import Command
from setuptools.command.install import install
#from setuptools.command.build_py import build_py
from pkg_resources import parse_requirements
from distutils.command.build import build as _build

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


CUSTOM_COMMANDS = [['echo', 'Custom command worked!']]

#class build(_build):
#    print("   ***      build         ")
#    sub_commands = _build.sub_commands + [('CustomCommands', None)]

class CustomCommands(Command):
      def initialize_options(self):
              pass

      def finalize_options(self):
              pass

      def RunCustomCommand(self, command_list):
           print('Running command: %s' % command_list)

      def run(self):
           print("        run         ")
           for command in CUSTOM_COMMANDS:
                self.RunCustomCommand(command)


class SystemBuild(_build):
    def run(self):
        print("********************** System Build")
        print(sysinstall_reqs)


class CustomInstall(install):
    def run(self):
        print("********************** Custom Install")

        sub_commands = _build.sub_commands + [('CustomCommands', None)]
        install.run(self)

"""
https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/complete/juliaset/setup.py

https://github.com/pypa/setuptool

https://www.anomaly.net.au/blog/running-pre-and-post-install-jobs-for-your-python-packages/

"""


setup(
 name="oxrange",
 version="0.0.3",
 author="Fazus Kazoo",
 description="Python things",
 long_description=long_description,
 long_description_content_type="text/markdown",
 dependency_links=[ "https://pypi.org/simple/" ],
 license="GPL",
 url="https://github.com/fazuskazoo/Orange",
 packages=["orange"],
 python_requires='>=3.6',
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
         cmdclass={
                   'CustomCommands': CustomCommands,
                   'install' : CustomInstall,
     },
)
