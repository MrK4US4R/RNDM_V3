import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from RENDOM import Main

        Main()

if bit == "64bit":
        from RENDOM_32 import Main

        Main()

