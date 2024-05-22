import os
import random
import platform
import ctypes
import subprocess

# Replace with the path to your image directory
directory = "/path/to/your/dir"

def change_wallpaper():
    wallpapers = os.listdir(directory)
    wallpaper = random.choice(wallpapers)
    wallpaper_path = os.path.join(directory, wallpaper)

    if platform.system() == "Windows":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
    elif platform.system() == "Linux":
        subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f "file://{wallpaper_path}"])
    else:
        print("Your operating system is not supported.")

change_wallpaper()
