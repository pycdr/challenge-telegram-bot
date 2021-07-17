from setuptools import setup
from pip._internal.req import parse_requirements

setup(
    name="anna",
    install_requires=parse_requirements("requirements.txt", session='hack')
)