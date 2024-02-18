from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dc_notifications',
    version='1.0.1',
    author="Calyx",
    description="Datareader Notifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias si las tienes
    ],
)