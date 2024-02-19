from importlib import resources

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# rinkrat version
__version__ = "0.1.1"

# config exposure
_cfg = tomllib.loads(resources.read_text("rinkrat", "config.toml"))

STANDINGS_BASE_URL = _cfg["standings"]["base_url"]
