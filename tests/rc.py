import asyncio
from shazamio import Shazam
import tkinter as tk
from tkinter import filedialog
import sys
sys.stdout.write("\x1b]2;FullTagz\x07")

async def main():
    root = tk.Tk()
    root.withdraw()

    path = list(filedialog.askopenfilenames(filetypes=[('MPEG Layer 3 Files','*.mp3')]))
    print(f' Number of Files: {len(path)}')
    path_len = int(len(path))
    if path_len == 0:
        print("Not Files Selected")
        exit(1)
    shazam = Shazam()
    out = await shazam.recognize_song(path[0])
    for i in range(path_len):
        path_len -= 1
        out = await shazam.recognize_song(path[path_len])
        try:
            print(f"Title: {out['track']['title']}")
            print(f"Artist: {out['track']['subtitle']}")
        except KeyError:
            print("One or More Metadata could not be found.")
        i += 1
        if i == path_len:
            print("[*] The Operation Completed!")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())