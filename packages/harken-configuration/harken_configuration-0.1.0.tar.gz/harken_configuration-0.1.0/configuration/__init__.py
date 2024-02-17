import sys

from funcy import lcat

from .configure import *

modules = ("configure",)
__all__ = lcat(sys.modules["configuration." + m].__all__ for m in modules)
