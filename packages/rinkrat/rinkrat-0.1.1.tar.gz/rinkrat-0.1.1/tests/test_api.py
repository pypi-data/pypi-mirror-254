import pytest

from rinkrat import api

def test_api_passing_empty_url():
    with pytest.raises(SystemExit):
        api.get("")

def test_api_passing_invalid_url():
    with pytest.raises(SystemExit):
        api.get("https://example.com/does/not/exist/")
