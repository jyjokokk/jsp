import tempfile

from typer.testing import CliRunner

from jspprint.cli import app

runner = CliRunner()


def test_csv_from_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("name,age\nAlice,30\nBob,25\n")
        f.flush()
        result = runner.invoke(app, ["--csv", f.name])
    assert result.exit_code == 0
    assert "Alice" in result.output
    assert "Bob" in result.output


def test_csv_custom_delimiter():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("a;b;c\n1;2;3\n")
        f.flush()
        result = runner.invoke(app, ["--csv", "-D", ";", f.name])
    assert result.exit_code == 0
    assert "1" in result.output


def test_csv_no_header():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("1,2,3\n4,5,6\n")
        f.flush()
        result = runner.invoke(app, ["--csv", "--no-header", f.name])
    assert result.exit_code == 0
    assert "1" in result.output
    assert "4" in result.output


def test_csv_requires_file():
    result = runner.invoke(app, ["--csv"])
    assert result.exit_code != 0
