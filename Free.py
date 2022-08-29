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

else:

            exit('\033[1;31m[×] WAIT KOREN SIR 32 BIT SOKALE UPLOAD HOBE')
