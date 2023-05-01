from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """"
    This function will return a list of string
    """
    requirements_list: List[str] = []

    with open(file_path) as file_obj:
        requirements_list = file_obj.readlines()
        requirements_list = [requirement.replace(
            "\n", "") for requirement in requirements_list]

    return requirements_list


setup(
    name="sensor",
    version='0.0.1',
    author="Raga_Santhosh",
    author_email="raga.j.santhosh@gmail.com",
    packages=find_packages(),
    # install_requires=["pymongo==4.2.0"]
    install_requires=get_requirements("requirements.txt")
)
