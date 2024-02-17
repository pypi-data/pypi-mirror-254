# Define statsframe version
from importlib_metadata import version as _v

# __version__ = "0.0.1"
__version__ = _v("statsframe")

del _v

# Import statsframe objects
# from ._tbl_data import *  # noqa: F401, F403, E402
# from ._databackend import *  # noqa: F401, F403, E402
from .datasummary import *  # noqa: F401, F403, E402
