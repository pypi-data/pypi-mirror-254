from setuptools import find_packages, setup

setup(
    name="meglio",
    version="0.0.1",
    author="Jason C.H",
    author_email="ctrysbita@outlook.com",
    packages=find_packages(),
    requires=[
        "perfetto",
    ],
)
