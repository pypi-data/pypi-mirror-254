from distutils.core import setup
from setuptools import find_packages

setup(
    name="omitron-owleye",
    version="0.0.0.01",
    description="Modules to support CADMUS operations.",
    author="Omitron Inc",
    author_email="CADMUS@omitron.com",
    url="https://omega3.omitron.com/projects/CADMUS/repos/project_cadmus",
    packages=find_packages(include=["lib"]),
)
