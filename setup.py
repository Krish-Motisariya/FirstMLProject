from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path)->List[str]:
    '''
        This function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(

    name='FirstMLProject',
    version='0.0.1',
    author='Krish',
    author_email='kdmotisariya19@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)