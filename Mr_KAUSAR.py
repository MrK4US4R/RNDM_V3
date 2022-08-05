import platform
b = platform.architecture()[0]
if b == '64bit':
    import Free_V3
if b == '32bit':
    import Free_V3
