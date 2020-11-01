#!/bin/python3

import os
import sys
import subprocess

def run():
    current = str(subprocess.check_output(["gsettings", "get", "org.gnome.desktop.background", "picture-uri"]))
    currentFileName = current.split("/")
    currentFileName = currentFileName[len(currentFileName) - 1].replace(r'\n', '').replace(r'"', '').replace(r"'", '')
    print(currentFileName)
    if len(sys.argv) < 2:
        os._exit(1)
    path = sys.argv[1]
    wallpapers = []
    position = 0
    for i, files in enumerate(os.listdir(path)):
        filePath = os.path.join(path, files)
        if os.path.isfile(filePath):
            wallpapers.append(filePath)
            if files == currentFileName:
                position = i
    next = position + 1
    if next > len(wallpapers) - 1:
        next = 0
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", wallpapers[next]])

if __name__ == "__main__":
    run()
