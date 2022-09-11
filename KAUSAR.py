import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from RANDOM_64 import Main;x
        Main()
        x()


if bit == "32bit":
        from RENDOM_32 import Main

        Main()
