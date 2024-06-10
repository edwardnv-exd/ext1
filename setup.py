from setuptools import setup, find_packages

setup(
    name="ext1",
    version="1",
    packages=find_packages(),
    install_requires=['numpy',],
    url="https://github.com/edwardnv-exd/ext1",
    author="Edward",
    author_email="edward_nv@exdion.com",
    description="Another simple hello package"
)
