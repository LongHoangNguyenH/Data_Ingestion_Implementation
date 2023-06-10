from setuptools import find_packages,setup
from typing import List
HYPHEN_MINUS_E_DOT = '-e .'


def get_requirements(path:str)->List[str]:
    require_item = []
    with open(path) as obj:
        require_item = obj.readlines()
        require_item = [item.replace("\n","")for item in require_item]

        if HYPHEN_MINUS_E_DOT in require_item: require_item.remove(HYPHEN_MINUS_E_DOT)
    return require_item

setup(
    name='Analyst_and_Choosing_the_best_model_project',
    version='0.1',
    author='Nguyen Hoang Long',
    author_email= 'longnh.uit@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)