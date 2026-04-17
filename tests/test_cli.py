import json

from click.testing import CliRunner

from ghostcall.cli import main


def test_clean_code_exits_zero():
    runner = CliRunner()
    result = runner.invoke(main, input="import json\njson.dumps({})\n")
    assert result.exit_code == 0
    assert "No hallucinations" in result.output


def test_hallucinated_code_exits_one():
    runner = CliRunner()
    result = runner.invoke(main, input="import json\njson.dumpss({})\n")
    assert result.exit_code == 1
    assert "json.dumpss" in result.output
    assert "dumps" in result.output


def test_json_output_is_valid():
    runner = CliRunner()
    result = runner.invoke(main, ["--json"], input="import json\njson.dumpss({})\n")
    assert result.exit_code == 1
    payload = json.loads(result.output)
    assert payload["summary"]["hallucinations_found"] == 1
    assert len(payload["findings"]) == 1
    finding = payload["findings"][0]
    assert finding["call"] == "json.dumpss"
    assert finding["missing_attr"] == "dumpss"
    assert "dumps" in finding["suggestions"]


def test_empty_input_handled():
    runner = CliRunner()
    result = runner.invoke(main, input="")
    assert result.exit_code == 0


def test_syntax_error_exits_two():
    runner = CliRunner()
    result = runner.invoke(main, input="def broken(\n")
    assert result.exit_code == 2
    assert "Syntax error" in result.output


def test_markdown_extraction():
    runner = CliRunner()
    md = "Look:\n```python\nimport json\njson.dumpss({})\n```\nDone.\n"
    result = runner.invoke(main, ["--md"], input=md)
    assert result.exit_code == 1
    assert "json.dumpss" in result.output


def test_markdown_no_python_blocks():
    runner = CliRunner()
    result = runner.invoke(main, ["--md"], input="just prose\n")
    assert result.exit_code == 0


def test_json_clean_code():
    runner = CliRunner()
    result = runner.invoke(main, ["--json"], input="import json\njson.dumps({})\n")
    assert result.exit_code == 0
    payload = json.loads(result.output)
    assert payload["summary"]["hallucinations_found"] == 0
    assert payload["findings"] == []
