import json
import tempfile

from typer.testing import CliRunner

from jsp.cli import app

runner = CliRunner()


def test_read_from_file():
    data = {"name": "test", "value": 42}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        f.flush()
        result = runner.invoke(app, [f.name])

    assert result.exit_code == 0
    assert '"name"' in result.output
    assert '"test"' in result.output


def test_read_from_stdin():
    data = {"hello": "world"}
    result = runner.invoke(app, input=json.dumps(data))
    assert result.exit_code == 0
    assert '"hello"' in result.output
    assert '"world"' in result.output


def test_no_input_shows_error():
    result = runner.invoke(app)
    assert result.exit_code != 0


def test_invalid_json_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write("not valid json")
        f.flush()
        result = runner.invoke(app, [f.name])

    assert result.exit_code != 0


def test_nonexistent_file():
    result = runner.invoke(app, ["/tmp/does_not_exist_jsp_test.json"])
    assert result.exit_code != 0


def test_nested_json():
    data = {"a": {"b": {"c": "deep"}}}
    result = runner.invoke(app, input=json.dumps(data))
    assert result.exit_code == 0
    assert '"deep"' in result.output
