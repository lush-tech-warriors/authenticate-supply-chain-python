# coding: utf-8

"""
    Authenticate Platform Supply Chain API

    Through this API you can Manage products and suppliers. Access to this API is restricted to authenticated users. Before accessing this API, first authenticate via the \"Account\" API. (https://uat-account.authenticateis.com/)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: platform-support@authenticateis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "authenticate-supply-chain"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Authenticate Platform Supply Chain API",
    author_email="platform-support@authenticateis.com",
    url="https://github.com/lush-tech-warriors/authenticate-supply-chain-python",
    keywords=["Swagger", "Authenticate Platform Supply Chain API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Through this API you can Manage products and suppliers. Access to this API is restricted to authenticated users. Before accessing this API, first authenticate via the \&quot;Account\&quot; API. (https://uat-account.authenticateis.com/)  # noqa: E501
    """
)
