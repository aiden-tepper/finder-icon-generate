import os
from openai import OpenAI

import tkinter as tk
from tkinter.filedialog import askdirectory
import subprocess

import sys

from applescript import tell

client = OpenAI()

def generate_image(name):
    prompt = f"art depicting a song called \"{name}\""
    response = client.images.generate(
        prompt=prompt,
        size="256x256",
        n=1
    )

    image_url = response.date[0].url

    return image_url

def create_icon_from_image(image_path, output_icon_path):
    # Create an .iconset directory
##    iconset_path = output_icon_path + ".iconset"
##    os.makedirs(iconset_path)
##
##    # Convert the image to an .icns file using iconutil
##    subprocess.run(["iconutil", "-c", "icns", "-o", iconset_path, image_path])
##
##    # Move the resulting .icns file to the desired location
##    icns_file = os.path.join(iconset_path, "icon.icns")
##    os.rename(icns_file, output_icon_path)
##
##    # Remove the temporary .iconset directory
##    os.rmdir(iconset_path)
    subprocess.run(["sips", "-s", "format", "icns", image_path, "--out", output_icon_path])


def change_folder_icon(folder_path, icon_path):
    # Change the folder icon using osascript
    script = f'tell application "Finder" to set icon file of (POSIX file \"{folder_path}\" as alias) to POSIX file \"{icon_path}\"'
    
    subprocess.run(["osascript", "-e", script])


folders = sys.argv[1:]

if not folders:
    print("Please provide file/directory paths.")
else:
    print(folders)
    for f in folders:
        name = f[2:]
##        image_url = generate_image(name)
##        print(image_url)
        icon_path = os.path.join(f, "folder_icon.icns")
        image_url = "./pic.png"
        create_icon_from_image(image_url, icon_path)
        change_folder_icon(f,icon_path)

        
##
##        # Change the folder's icon to the generated image
##        change_icon(folder, image_url)
