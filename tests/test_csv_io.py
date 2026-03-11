import tempfile

import pytest

from jspprint.csv_io import print_csv, read_csv


class TestReadCsv:
    def test_read_basic(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("a,b,c\n1,2,3\n")
            f.flush()
            rows = read_csv(f.name)
        assert rows == [["a", "b", "c"], ["1", "2", "3"]]

    def test_read_custom_delimiter(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("a;b;c\n1;2;3\n")
            f.flush()
            rows = read_csv(f.name, delimiter=";")
        assert rows == [["a", "b", "c"], ["1", "2", "3"]]

    def test_nonexistent_file(self):
        with pytest.raises(FileNotFoundError):
            read_csv("/tmp/does_not_exist_csv_test.csv")


class TestPrintCsv:
    def test_empty_rows(self, capsys):
        print_csv([])
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_with_header(self, capsys):
        print_csv([["name", "age"], ["Alice", "30"]])
        captured = capsys.readouterr()
        assert "name" in captured.out
        assert "Alice" in captured.out

    def test_without_header(self, capsys):
        print_csv([["1", "2"], ["3", "4"]], header=False)
        captured = capsys.readouterr()
        assert "1" in captured.out
        assert "3" in captured.out
