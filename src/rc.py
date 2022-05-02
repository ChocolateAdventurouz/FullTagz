import asyncio
from shazamio import Shazam
import tkinter as tk
from tkinter import filedialog
import mutagen
from mutagen.easyid3 import EasyID3







def tag(path, title, artist, path_len):
    for i in range(path_len):
        try:
            meta = EasyID3(path[0])

        except mutagen.id3.ID3NoHeaderError:
            meta = mutagen.File(path_len, easy=True)
            meta.add_tags()
        meta['title'] = title
        meta['artist'] = artist
        meta.save(path_len, v1=2)
        path_len -=1
        meta = EasyID3(path[path_len])
        i += 1

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
    try:
        meta = EasyID3(path[0])
    except mutagen.id3.ID3NoHeaderError:
        meta = mutagen.File(path_len, easy=True)
        meta.add_tags()
    for i in range(path_len):
        path_len -= 1
        out = await shazam.recognize_song(path[path_len])
        try:
            meta = EasyID3(path[path_len])
        except mutagen.id3.ID3NoHeaderError:
            meta = mutagen.File(path_len, easy=True)
            meta.add_tags()
        try:
            title = out['track']['title']
            artist = out['track']['subtitle']
            print(f"Title: {out['track']['title']}")
            print(f"Artist: {out['track']['subtitle']}")
            meta['title'] = title
            meta['artist'] = artist
            meta.save(path[path_len], v1=2)
            meta = EasyID3(path[path_len])


        except KeyError:
            print("One or More Metadata could not be found.")
        i += 1
        if i == path_len:
            print("[*] The Operation Completed!")
        