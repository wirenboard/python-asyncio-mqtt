# SPDX-License-Identifier: BSD-3-Clause
from setuptools import find_packages, setup

setup(
    name="asyncio_mqtt",
    version="2.3.1",
    packages=find_packages(),
    package_data={
        "asyncio_mqtt": ["py.typed"],
    },
    url="https://github.com/sbtinstruments/asyncio-mqtt",
    author="Frederik Aalund",
    author_email="fpa@sbtinstruments.com",
    description="Idomatic asyncio wrapper around paho-mqtt.",
    license="BSD 3-clause License",
    license_files=("LICENSE",),
    keywords="mqtt async asyncio paho-mqtt wrapper",
)
