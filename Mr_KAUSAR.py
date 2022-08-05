import platform
b = platform.architecture()[0]
if b == '64bit':
    import FreeV3
if b == '32bit':
    import FreeV3
