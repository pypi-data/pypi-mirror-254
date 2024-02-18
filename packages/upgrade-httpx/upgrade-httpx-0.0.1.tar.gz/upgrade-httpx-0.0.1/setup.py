from setuptools import setup, find_packages

setup(
    name="upgrade-httpx",
    version="0.0.1",
    packages=['httpx'],
    install_requires = [
        "requests==2.31.0"
    ],
    author="upgrade-httpx",
    description="upgrade-httpx"
)