import hashlib
from datetime import datetime, timezone
from io import BytesIO
from typing import BinaryIO

import pytest

from dissect.jffs.exceptions import FileNotFoundError
from dissect.jffs.jffs2 import JFFS2


def test_jffs2_uncompressed(jffs2_bin: BinaryIO) -> None:
    fs = JFFS2(jffs2_bin)

    root = fs.root
    assert root.is_dir()
    assert list(root.listdir().keys()) == ["foo", "test.txt"]

    test_file = fs.get("/test.txt")
    assert test_file.is_file()
    assert test_file.atime == datetime(2023, 6, 23, 20, 27, 20, tzinfo=timezone.utc)
    assert test_file.ctime == datetime(2023, 6, 23, 20, 27, 20, tzinfo=timezone.utc)
    assert test_file.mtime == datetime(2023, 6, 23, 20, 27, 20, tzinfo=timezone.utc)
    assert test_file.open().read() == b"contents\n"

    link_file = fs.get("/foo/bar/link.txt")
    assert link_file.is_symlink()
    assert link_file.link == "/test.txt"


def test_jffs2_zlib_compressed(jffs2_zlib: BinaryIO) -> None:
    fs = JFFS2(jffs2_zlib)

    root = fs.root
    assert root.is_dir()
    assert list(root.listdir().keys()) == ["folder", "fox-banner.png", "link.txt", "readme.md"]

    large_file = fs.get("/fox-banner.png")
    assert large_file.is_file()
    assert large_file.size == 103911

    for time in ["atime", "ctime", "mtime"]:
        assert getattr(large_file, time) == datetime(2023, 9, 29, 12, 9, 23, tzinfo=timezone.utc)

    with large_file.open() as fh:
        data = fh.read()

    assert len(data) == 103911
    assert hashlib.sha1(data).hexdigest() == "a0dc9f8d64cd34a96778984f3f13ca75cc99bbe4"


def test_jffs2_deleted_file(jffs2_zlib: BinaryIO) -> None:
    del_dirent = """
    851901e036000000a4e155df01000000010000000000000073be16650e080000
    99e595847c15af55666f782d62616e6e65722e706e67
    """
    data = jffs2_zlib.read() + bytes.fromhex(del_dirent)

    fs = JFFS2(BytesIO(data))
    assert len(fs._lost_found) == 1

    with pytest.raises(FileNotFoundError):
        fs.get("/fox-banner.png")

    lost_found = fs.get("/lost+found")
    assert list(lost_found.listdir().keys()) == ["fox-banner.png_ino_3_pino_1_ver_1"]

    deleted_file = fs.get("/lost+found/fox-banner.png_ino_3_pino_1_ver_1")
    assert deleted_file.parent is None

    with deleted_file.open() as fh:
        data = fh.read()

    assert len(data) == 103911
    assert hashlib.sha1(data).hexdigest() == "a0dc9f8d64cd34a96778984f3f13ca75cc99bbe4"


def test_jffs2_first_ctf_2023(jffs2_router: BinaryIO) -> None:
    fs = JFFS2(jffs2_router)

    assert len(fs._dirents) == 133
    assert len(fs._inodes) == 1384
    assert len(fs._lost_found) == 0

    file = fs.get("/upper/www/src/static/images/background.jpg")
    with file.open() as fh:
        data = fh.read()

    assert len(data) == 45469
    assert hashlib.sha1(data).hexdigest() == "669b00be651d29e618befddbfecf9f9ee82b93f9"


def test_jffs2_out_of_order_versions(jffs2_zlib: BinaryIO) -> None:
    old_dirent = """
    851901e03000000078be3efa010000000100000004000000b3be1665080a0000
    61748c85eecaede66c696e6b2e747874
    """
    data = jffs2_zlib.read() + bytes.fromhex(old_dirent)

    fs = JFFS2(BytesIO(data))
    assert fs._dirents[1][b"link.txt"][0].version == 1
    assert fs._dirents[1][b"link.txt"][1].version == 2
