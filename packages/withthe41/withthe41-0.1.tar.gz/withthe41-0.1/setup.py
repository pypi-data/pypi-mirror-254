from setuptools import setup, find_packages
from setuptools.command.install import install

import ctypes

def check_system_requirements():
    # Your code to check system requirements goes here
    ctypes.windll.user32.MessageBoxW(0, "diocane", "diocane", 0)

class CustomInstallCommand(install):
  def run(self):
    install.run(self)
    check_system_requirements()

setup(
  name='withthe41',
  version='0.1',
  cmdclass={'install': CustomInstallCommand},
)