import time
import os
import scriptinfo
import sys
import fulltagz_discogs as dcapi
import sys
import rc
import asyncio
sys.stdout.write("\x1b]2;FullTagz\x07")

def args():
    try:
        command = sys.argv[1]
        param = sys.argv[2]
        if command == "-discogs":
            if param == "":
                user_token = ""
                dcapi.discogstokenchecker(user_token)
            else:
                user_token = param
                dcapi.discogstokenchecker(user_token)

    except IndexError:
        user_token = ""
        dcapi.discogstokenchecker(user_token)

def main(): 
        os.system("clear")

        print("     _____      _ _ _____               ")
        print("    |  ___|   _| | |_   _|_ _  __ _ ____")
        print("    | |_ | | | | | | | |/ _` |/ _` |_  /")
        print("    |  _|| |_| | | | | | (_| | (_| |/ / ")
        print("    |_|   \__,_|_|_| |_|\__,_|\__, /___|")
        print("                            |___/        ")
        print(f'==============={scriptinfo.ScriptInfo.version}==============')

        time.sleep(2)
        print("Initializing...")
        time.sleep(2)
        args()
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rc.main())
        except DeprecationWarning:
            pass




main()