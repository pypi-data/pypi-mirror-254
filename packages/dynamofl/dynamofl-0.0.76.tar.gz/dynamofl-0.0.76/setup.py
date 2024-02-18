"""
Defines the Python package setup for the dynamofl package.
"""
import os

from setuptools import find_namespace_packages, setup

_VERSION = os.environ.get("BUILD_VERSION_CORE")
try:
    assert _VERSION is not None
except AssertionError:
    warning_msg = (
        "BUILD_VERSION_CORE environment variable not set. Please set it to the "
        "version of the package you are building. Example: export BUILD_VERSION_CORE=0.0.67. "
        "Using default version 0.0.67"
    )
    print(f"\033[91m {'WARNING'}\033[00m {warning_msg}")
    _VERSION = "0.0.67"

setup(
    name="dynamofl",
    version="0.0.76",
    author="Emile Indik",
    long_description="DynamoFL Core Python Client",
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "requests==2.31.0",
        "websocket-client==1.5.0",
        "shortuuid==1.0.11",
    ],
)
