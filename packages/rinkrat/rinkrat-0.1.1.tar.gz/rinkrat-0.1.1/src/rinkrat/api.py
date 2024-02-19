import requests
import requests_cache
from datetime import timedelta

import sys as _sys

requests_cache.install_cache(
    'rinkrat_cache',
    'sqlite',
    use_cache_dir=True,
    expire_after = timedelta(0, 0, 0, 0, 5.0, 0, 0)
)

def get(url: str, params=None, **kwargs) -> dict:
    """
    Make a GET request to the provided url and return the results
    as a json encoded object.
    """
    try:
        response = requests.get(url, params=params, **kwargs)
        response.raise_for_status()

        try:
            result = response.json()
            return result
        except requests.exceptions.JSONDecodeError as e:
            _sys.stderr.write(f"{__name__}: {e}\n")
            raise SystemExit()

    except requests.exceptions.RequestException as e:
        _sys.stderr.write(f"{__name__}: {e}\n")
        raise SystemExit()
