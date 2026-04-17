from ghostcall.markdown import extract_python


def test_extract_single_python_block():
    md = """
Some prose here.

```python
import json
json.dumps({})
```

More prose.
"""
    assert "import json" in extract_python(md)
    assert "json.dumps" in extract_python(md)


def test_multiple_blocks_concatenated():
    md = """
```python
a = 1
```

```py
b = 2
```
"""
    out = extract_python(md)
    assert "a = 1" in out
    assert "b = 2" in out


def test_non_python_blocks_ignored():
    md = """
```javascript
const x = 1;
```

```python
y = 2
```
"""
    out = extract_python(md)
    assert "const x" not in out
    assert "y = 2" in out


def test_no_blocks_returns_empty():
    assert extract_python("just prose, no code.") == ""


def test_case_insensitive_language_tag():
    md = """
```Python
z = 3
```
"""
    assert "z = 3" in extract_python(md)
