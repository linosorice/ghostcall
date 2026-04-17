from ghostcall.parser import parse


def test_import_alias_resolves_to_real_module():
    src = "import pandas as pd\npd.DataFrame.to_jsonl()\n"
    r = parse(src)
    assert r.imports["pd"].module == "pandas"
    assert r.imports["pd"].attr is None
    assert len(r.calls) == 1
    assert r.calls[0].raw_chain == ["pd", "DataFrame", "to_jsonl"]
    assert r.calls[0].resolved_chain == ["pandas", "DataFrame", "to_jsonl"]
    assert r.calls[0].lineno == 2


def test_from_import_resolves_to_module_attr():
    src = "from pandas import DataFrame\nDataFrame.to_jsonl()\n"
    r = parse(src)
    assert r.imports["DataFrame"].module == "pandas"
    assert r.imports["DataFrame"].attr == "DataFrame"
    assert r.calls[0].resolved_chain == ["pandas", "DataFrame", "to_jsonl"]


def test_from_import_with_alias():
    src = "from pandas import DataFrame as DF\nDF.to_jsonl()\n"
    r = parse(src)
    assert r.imports["DF"].module == "pandas"
    assert r.imports["DF"].attr == "DataFrame"
    assert r.calls[0].resolved_chain == ["pandas", "DataFrame", "to_jsonl"]


def test_plain_import():
    src = "import os\nos.path.joinpath('a', 'b')\n"
    r = parse(src)
    assert r.imports["os"].module == "os"
    assert r.calls[0].resolved_chain == ["os", "path", "joinpath"]


def test_unknown_root_skipped():
    src = "x = 1\nx.foo()\n"
    r = parse(src)
    assert len(r.calls) == 0


def test_outermost_chain_only():
    src = "import pandas as pd\npd.DataFrame.to_jsonl()\n"
    r = parse(src)
    # Should not also report `pd.DataFrame` as a separate finding
    assert len(r.calls) == 1


def test_star_import_recorded():
    src = "from os import *\n"
    r = parse(src)
    assert "os" in r.star_imports


def test_relative_import_skipped():
    src = "from . import foo\n"
    r = parse(src)
    assert r.imports == {}


def test_chain_from_method_call_skipped():
    # We can't statically know what a function call returns
    src = "import pandas as pd\npd.DataFrame().to_jsonl()\n"
    r = parse(src)
    # `pd.DataFrame` should still be picked up (it's the outermost Attribute before the Call)
    chains = [c.resolved_chain for c in r.calls]
    assert ["pandas", "DataFrame"] in chains


def test_multiple_imports_same_module():
    src = """
import json
import os.path
json.dumps({})
os.path.join('a', 'b')
"""
    r = parse(src)
    assert r.imports["json"].module == "json"
    assert r.imports["os"].module == "os"
    chains = {tuple(c.resolved_chain) for c in r.calls}
    assert ("json", "dumps") in chains
    assert ("os", "path", "join") in chains
