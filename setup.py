from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requiremets(file_path) -> List[str]:
    reqirements = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirement]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 

    return requirements

setup(
    name = 'RegressorProject',
    version = '0.0.1',
    author = 'Athul',
    author_email = 'vathul69.va@gmail.com',
    install_requires = get_requiremets("requirements.txt"),
    packages = find_packages()

)