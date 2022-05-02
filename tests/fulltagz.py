from ast import Import


try:
    import discogs_client
    from shazamio import Shazam
    import time
    import os
    import asyncio
    import sys
    import fulltagz_discogs as dcapi
    shazam = Shazam()
    args = sys.argv[1]
    def tag(title, artist, albumartist, year, coverart, gerne, track, album):
        return


    def loader(): 

        os.system("clear")
        print("     _____      _ _ _____               ")
        print("    |  ___|   _| | |_   _|_ _  __ _ ____")
        print("    | |_ | | | | | | | |/ _` |/ _` |_  /")
        print("    |  _|| |_| | | | | | (_| | (_| |/ / ")
        print("    |_|   \__,_|_|_| |_|\__,_|\__, /___|")
        print("                            |___/        ")
        print("===============Version 1.0.0==============")

        time.sleep(2)
        print("Initializing...")
        time.sleep(2)

    async def main():
        out = await shazam.recognize_song('track.mp3')
        print(out)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    def main():
        if args == "-discogs":
            loader()
            user_token = ""
            dcapi.discogstokenchecker(user_token)
        elif args == "-f":
            loader()






























    main()


    """   discogstokenchecker()
        elif args == "-f":
            print("Please specify the filename.")
            return;
        elif args == "-f "+ file_arg:
            print(0)"""

except IndexError:
    pass