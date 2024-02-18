import setuptools
import os
import time

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '0.0.3'

postfix = "" if os.getenv("RELEASE", "0") == "1" else ".dev%s" % round(time.time())


setuptools.setup(
    name="deser",
    version=f"{version}{postfix}",
    description="Serializer/deserializer to object",
    author="Rafał Zarajczyk",
    author_email="rzarajczyk@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rzarajczyk/service-bootstrap",
    keywords=[],
    packages=['deser'],
    package_dir={'deser': './deser'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
