from setuptools import setup, find_packages

with open("requirements.txt","r") as f:
    requirements = f.read().splitlines()

setup(
    name="mlops_first_project",
    version="0.1.0",
    author="Utkarsh 05",
    packages=find_packages(),
    install_requires=requirements,
)