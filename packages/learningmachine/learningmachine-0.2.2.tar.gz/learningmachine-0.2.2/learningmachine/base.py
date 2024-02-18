from rpy2.robjects import r
from rpy2.robjects.packages import importr
from .utils import check_install_r_pkg

base = importr("base")
stats = importr("stats")


class Base(object):
    """
    Base class.
    """

    def __init__(self):
        """
        Initialize the model.
        """
        self.obj = None
