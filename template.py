#!/usr/bin/env python3
import re
import sys
from pathlib import Path

import requests


DEBIANS = {
    'ubuntu:lucid',
    'ubuntu:precise',
    'ubuntu:trusty',
    'ubuntu:xenial',
    'debian:wheezy',
    'debian:jessie',
    'debian:stretch',
}
DEBIAN_TEMPLATE = open('debian.Dockerfile').read()


def dumb_init_versions():
    """List of versions, most recent first."""
    req = requests.get('https://api.github.com/repos/Yelp/dumb-init/releases')
    versions = []

    for version in req.json():
        tag = version['tag_name']
        assert re.match('v([0-9]+\.)+[0-9]+', tag), tag
        versions.append(tag[1:])

    return sorted(
        versions,
        key=lambda tag: tag.split('.'),
        reverse=True,
    )


def build_debian(tag, debian, version):
    d = Path(tag)
    try:
        d.mkdir()
    except FileExistsError:
        pass
    dockerfile = (d / 'Dockerfile')
    with dockerfile.open('w') as f:
        f.write(
            DEBIAN_TEMPLATE.format(
                source=debian,
                version=version,
            ),
        )


def main():
    versions = dumb_init_versions()
    for debian in DEBIANS:
        debian_tag = debian.replace(':', '-')

        # latest version
        build_debian(debian_tag, debian, versions[0])


if __name__ == '__main__':
    sys.exit(main())
