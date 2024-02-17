import gzip
import os

import pytest


def absolute_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def gzip_file(filename):
    with gzip.GzipFile(absolute_path(filename), "rb") as fh:
        yield fh


@pytest.fixture
def jffs2_bin():
    yield from gzip_file("data/jffs2.bin.gz")


@pytest.fixture
def jffs2_zlib():
    yield from gzip_file("data/jffs2.zlib.bin.gz")


@pytest.fixture
def jffs2_router():
    yield from gzip_file("data/router.bin.gz")
