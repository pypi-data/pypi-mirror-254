from comfyconf.readers import available_readers, PyYaml, Ruamel, get_reader
from pathlib import Path
import pytest


class TestPyYaml:
    test_object = PyYaml("test_path.yaml")

    def test_init(self):
        assert self.test_object.config_path == Path("test_path.yaml")

    def test_raise_filenotfound(self):
        with pytest.raises(FileNotFoundError):
            self.test_object.read()

    def test_reads_file(self):
        test_content = """line1: 'A'"""
        path = Path("test.yaml")
        obj = PyYaml(path)

        with open(path, "w") as f:
            f.write(test_content)

        try:
            assert obj.read() == {"line1": "A"}
        finally:
            path.unlink()


class TestRuamelYaml:
    test_object = Ruamel("test_path.yaml")

    def test_init(self):
        assert self.test_object.config_path == Path("test_path.yaml")

    def test_raise_filenotfound(self):
        with pytest.raises(FileNotFoundError):
            self.test_object.read()

    def test_reads_file(self):
        test_content = """line1: 'A'"""
        path = Path("test.yaml")
        obj = Ruamel(path)

        with open(path, "w") as f:
            f.write(test_content)

        try:
            assert obj.read() == {"line1": "A"}
        finally:
            path.unlink()


class TestGetReader:
    def test_valid_readers(self):
        for key, value in available_readers.items():
            assert get_reader(key) == value

    def test_invalid_reader(self):
        with pytest.raises(ValueError):
            get_reader("not_a_reader")
