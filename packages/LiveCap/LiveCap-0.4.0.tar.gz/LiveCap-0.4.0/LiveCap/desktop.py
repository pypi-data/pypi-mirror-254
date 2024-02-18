import platform
from .capture import Capture
from .Capture import DXGICapture, GDICapure, WindowsGraphicsCapture


class DesktopCapture(Capture):
    def __new__(cls, *args, **kwargs):
        if not args and not kwargs:
            return DXGICapture()
        elif args or kwargs:
            version = platform.platform().split('-')
            if (len(args) < 2 and not kwargs.get('scale')) or version[1] == '10' and int(
                    version[2].split('.')[2][:2]) > 19:
                return WindowsGraphicsCapture(*args, **kwargs)
            return GDICapure(*args, **kwargs)
