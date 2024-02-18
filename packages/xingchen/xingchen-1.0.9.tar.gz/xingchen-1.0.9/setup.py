# coding: utf-8

"""
    通义星尘开放接口Python SDK，详情可以参考官方文档 https://tongyi.aliyun.com/xingchen/document

"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "xingchen"
VERSION = "1.0.9"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum",
    "sseclient-py >= 1.8.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="XingChen 开放接口定义",
    author="zhiyong.fzy",
    author_email="zhiyong.fzy@alibaba-inc.com",
    url="",
    keywords=["XingChen", "Character AI", "XingChen开放接口定义"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests", "demo"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    通义星尘(https://tongyi.aliyun.com/xingchen) Python SDK 
    """,  # noqa: E501
    package_data={"xingchen": ["py.typed"]},
)
