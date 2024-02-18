from setuptools import setup, find_packages
from pip._internal.req import req_file
from setuptools.glob import glob

VERSION = '0.0.3.28'
DESCRIPTION = 'aslib 相关python包'
requirments = req_file.parse_requirements('requirements.txt', session='hack')
instll_requires = [req.requirement for req in requirments]

print(instll_requires)

setup(
    name="ascript",
    version=VERSION,
    author="aojoy",
    author_email="aojoytec@163.com",
    description=DESCRIPTION,
    include_package_data=True,

    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding="UTF8").read(),
    packages=find_packages(),
    keywords=['python', "aslib"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://airscript.cn/",
    install_requires=instll_requires,
)
