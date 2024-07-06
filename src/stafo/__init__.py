
try:
    from .core import *
except ImportError as ex:
    # ignoring import errors might be relevant during the installation process
    # where we need the version but requirements might not yet be installed.
    print(f"Ignoring the following exception: {ex}")
    pass

from .release import __version__
