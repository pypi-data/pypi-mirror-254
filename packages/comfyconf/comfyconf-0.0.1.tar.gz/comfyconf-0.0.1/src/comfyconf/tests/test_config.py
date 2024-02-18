from comfyconf.config import DotDict, make_config
from comfyconf.readers import available_readers

import pytest
from pathlib import Path


def make_file(test_content, path):
    with open(path, "w") as f:
        f.write(test_content)


class TestDotDict:
    def test_simple_dict(self):
        test = DotDict({"a": "b"})
        assert test.a == "b"

    def test_nested_dict(self):
        test = DotDict({"a": {"b": "c"}})
        assert test.a.b == "c"

    def test_key_not_present(self):
        test = DotDict({"a": "b"})
        with pytest.raises(KeyError):
            test.c

    def test_numerical_key_error(self):
        with pytest.raises(ValueError):
            DotDict({1: "b"})

    def test_nested_numerical_key_error(self):
        with pytest.raises(ValueError):
            DotDict({"a": {1: "b"}})


class TestMakeConfig:
    def test_simple_config(self):
        path = Path("test.yaml")
        content = """a: b"""
        make_file(content, path)

        try:
            for reader in available_readers.keys():
                config = make_config(path, reader)
                assert config.a == "b"
        finally:
            path.unlink()

    def test_nested_config(self):
        path = Path("test.yaml")
        content = """
        a: 
          b: c 
        """
        make_file(content, path)
        try:
            for reader in available_readers.keys():
                config = make_config(path, reader)
                assert config.a.b == "c"
        finally:
            path.unlink()
