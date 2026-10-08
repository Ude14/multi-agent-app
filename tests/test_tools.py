import pytest
from src.tools.search import run_custom_tool

def test_run_custom_tool_success():
    result = run_custom_tool("Python")
    assert "Python" in result

def test_run_custom_tool_empty():
    with pytest.raises(ValueError):
        run_custom_tool("")