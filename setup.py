from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME= 'requirements.txt'
HYPHEN_E_DOT = '-e .'

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        requirements_list = requirements_file.readlines()
    requirements_list = [requirement_name.replace("\n","") for requirement_name in requirements_list]
    
    if HYPHEN_E_DOT in requirements_list:
        requirements_list.remove(HYPHEN_E_DOT)

setup(
    name = 'Sensor',
    version = '0.0.2',
    author='Uday',
    author_email='udaysd01@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements(),
)