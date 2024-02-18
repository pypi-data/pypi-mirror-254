from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="microgue",
    version="4.0.0",
    author="Michael Hudelson",
    author_email="michaelhudelson@gmail.com",
    description="This project contains bootstrap code to speed up the development of AWS based microservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=[
        "microgue",
        "microgue.storages",
        "microgue.loggers",
        "microgue.security",
        "microgue.secrets",
        "microgue.constants",
        "microgue.models",
        "microgue.queues",
        "microgue.events",
        "microgue.services",
        "microgue.caches"
    ],
    install_requires=[
        "boto3",
        "flask",
        "flask-classful",
        "redis",
        "requests"
    ],
    python_requires=">=3.7",
)
