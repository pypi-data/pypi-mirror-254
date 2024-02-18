from setuptools import setup, find_packages

#leer el contenido de README.md 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="TestHack4u",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[],
    author="1FeeirG",
    description="Una biblioteca para consultar todos los cursos existentes de hack4u",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io",
)
