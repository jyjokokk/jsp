from typer.testing import CliRunner

from jsp.cli import app

runner = CliRunner()


def test_main():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello from jsp!" in result.output
