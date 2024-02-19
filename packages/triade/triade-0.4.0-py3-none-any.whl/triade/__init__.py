from importlib.metadata import version


try:
    __version__ = version("triade")
except ModuleNotFoundError:
    __version__ = None
