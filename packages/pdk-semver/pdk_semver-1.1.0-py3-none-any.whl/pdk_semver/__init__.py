try:
    from .__version__ import __version__
except Exception:
    # editable install during development
    __version__ = "0.1.0"


__all__ = ["__version__"]
