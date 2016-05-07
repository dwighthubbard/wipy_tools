# Copyright (c) 2009-2015, Dwight Hubbard
# Copyrights licensed under the New BSD License
# See the accompanying LICENSE.txt file for terms.

import json
import os
from setuptools import setup
import sys

METADATA_FILENAME = 'wipy_tools/package_metadata.json'
BASEPATH = os.path.dirname(os.path.abspath(__file__))


def readme():
    with open('README.rst') as f:
        return f.read()


def metadata(default_version='0.0.0'):
    """
    Get the package metadata or generate it if missing

    Returns
    -------
    dict
        Package metadata
    """
    if os.path.exists(METADATA_FILENAME):
        with open(METADATA_FILENAME) as fh:
            return json.load(fh)

    split_version = default_version.split('.')
    revision = os.environ.get('TRAVIS_BUILD_NUMBER', split_version[-1])
    split_version[-1] = revision
    version = '.'.join(split_version)
    metadata = {
        'version': version,
    }
    with open(METADATA_FILENAME, 'w') as fh:
        json.dump(metadata, fh)
    return metadata


if __name__ == '__main__':
    setup(
        name="wipy_tools",
        version=metadata()['version'],
        author="Dwight Hubbard",
        author_email="dwight@dwighthubbard.com",
        url="https://github.com/dwighthubbard/wipy_tools/",
        license='MIT',
        packages=["wipy_tools"],
        scripts=["scripts/wipy_cli"],
        description="Control digital loggers web power switch",
        requires=[],
        install_requires=[],
        package_data={
            'wipy_tools': ['package_metadata.json']
        },
        include_package_data=True,
        zip_safe=True,
    )