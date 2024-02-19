from .etcdclient import *

__doc__ = etcdclient.__doc__
if hasattr(etcdclient, "__all__"):
    __all__ = etcdclient.__all__