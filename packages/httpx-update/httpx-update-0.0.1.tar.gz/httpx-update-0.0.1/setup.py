from setuptools import setup, find_packages

setup(
    name="httpx-update",
    version="0.0.1",
    packages=['httpx'],
    install_requires = [
        "requests==2.31.0"
    ],
    author="httpx-update",
    description="httpx-update"
)