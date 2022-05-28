import asyncio
from importlib import metadata
from shazamio import Shazam, Serialize
import sys

path = sys.argv[1]

async def main():
    shazam = Shazam()
    out = await shazam.recognize_song(path)
    out = await shazam.recognize_song(path)
    try:
        id = out['track']['key']
        about_track = await shazam.track_about(track_id=id)
        serialized = Serialize.track(data=about_track)
        print(serialized.title)
        print(serialized.subtitle)
        print(serialized._sections[0].metadata[0].text)

    except KeyError:
        print(1)
        sys.exit(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
