# coding: utf8
""" 
@File: setup.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-07
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import setuptools
from datetime import datetime
import subprocess

# package name
name = "PyFairyland"

# version
major_number = 0
sub_number = 0
stage_number = 3
revise_number = 37

# leng desctiption
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


if revise_number.__str__().__len__() < 5:
    nbit = 5 - revise_number.__str__().__len__()
    revise_number = "".join((("0" * nbit), revise_number.__str__()))
else:
    revise_number = revise_number.__str__()
date_number = datetime.now().date().__str__().replace("-", "")
revise_after = "-".join((revise_number.__str__(), date_number))

# version: (release_version, test_version, alpha_version, beta_version)
release_version = ".".join((major_number.__str__(), sub_number.__str__(), stage_number.__str__()))
test_version = ".".join((release_version, "".join(("rc", revise_after))))
alpha_version = ".".join((release_version, "".join(("alpha", revise_after))))
beta_version = ".".join((release_version, "".join(("beta", revise_after))))


class InstallDependenciesCommand(setuptools.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = "python -m pip install --force git+https://github.com/imba-tjd/pip-autoremove@ups"
        subprocess.call(command, shell=True)


# version: (release_version, test_version, alpha_version, beta_version)
setuptools.setup(
    name=name,
    fullname="".join((name, release_version)),
    keywords=["fairyland", "Fairyland", "pyfairyland", "PyFairyland", "fairy", "Fairy"],
    version=test_version,
    author="Austin D",
    author_email="fairylandhost@outlook.com",
    description="Austin personally developed Python library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AustinFairyland/AustinFairylandRepository",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: SQL",
        "Framework :: Django :: 2",
        "Framework :: Django :: 3",
        "Framework :: Django :: 4",
        "Framework :: Flask",
        "Framework :: FastAPI",
        "Framework :: Flake8",
        "Framework :: IPython",
        "Framework :: Jupyter",
        "Framework :: Scrapy",
        "Natural Language :: English",
        "Natural Language :: Chinese (Simplified)",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: System :: Operating System Kernels :: Linux",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pip-review",
        "pip-autoremove",
        "python-dotenv",
        "loguru",
        "pymysql",
        "psycopg2-binary",
        "requests",
        "tornado",
        "pandas",
        "django",
        # "django<5.0.0",
        "django-stubs",
        "djangorestframework",
        "django-cors-headers",
    ],
    cmdclass={
        "install_dependencies": InstallDependenciesCommand,
    },
)
