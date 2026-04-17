from ghostcall.checker import HALLUCINATED, MODULE_MISSING, OK, check
from ghostcall.parser import CallInfo


def _call(*chain, lineno=1):
    return CallInfo(
        raw_chain=list(chain),
        resolved_chain=list(chain),
        lineno=lineno,
        col_offset=0,
    )


def test_real_method_passes():
    r = check(_call("json", "dumps"))
    assert r.status == OK


def test_hallucinated_method_detected():
    r = check(_call("json", "dump_string"))
    assert r.status == HALLUCINATED
    assert r.missing_attr == "dump_string"
    assert r.parent_display == "json"


def test_hallucinated_with_suggestions():
    r = check(_call("json", "dumpss"))
    assert r.status == HALLUCINATED
    assert "dumps" in r.suggestions


def test_uninstalled_module_marked_separately():
    r = check(_call("definitely_not_a_real_module_xyz", "anything"))
    assert r.status == MODULE_MISSING


def test_submodule_loaded_on_demand():
    # importlib loads submodules on attribute access only sometimes
    r = check(_call("os", "path", "join"))
    assert r.status == OK


def test_deep_chain_into_class_method():
    # `pathlib.Path.exists` is a real bound method
    r = check(_call("pathlib", "Path", "exists"))
    assert r.status == OK


def test_deep_chain_with_hallucinated_method():
    r = check(_call("pathlib", "Path", "fake_method_xyz"))
    assert r.status == HALLUCINATED
    assert r.missing_attr == "fake_method_xyz"
