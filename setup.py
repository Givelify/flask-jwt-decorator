from setuptools import find_packages, setup

setup(
    name="givelifyjwtdecorator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=3.1.0",
        "PyJWT>=2.10.1",
    ],
    description="Pluggable JWT authentication middleware for Flask",
    author="Me",
    python_requires=">=3.12",
)
