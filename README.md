This Python script allows you to change your desktop wallpaper randomly from a directory containing image files. It supports both Windows and Linux operating systems.

## Prerequisites

For Windows:
- No additional prerequisites are required.

For Linux:
- The `gsettings` command-line tool should be installed. It is typically included in most Linux distributions.

## Usage

1. Open the script in a text editor.
2. Replace `/path/to/your/dir` with the actual path to the directory containing your wallpaper images.
3. Save the script and run it using a Python interpreter.

The script will randomly select an image from the specified directory and set it as your desktop wallpaper.

## How it Works

The script defines a function called `change_wallpaper()` that performs the following steps:

1. It uses `os.listdir(directory)` to get a list of all files in the specified directory.
2. It randomly selects a file from the list using `random.choice(wallpapers)`.
3. It constructs the full path of the selected wallpaper file using `os.path.join(directory, wallpaper)`.
4. It checks the operating system using `platform.system()`.
5. If the operating system is Windows, it uses the `ctypes` module to call the `SystemParametersInfoW` function from the Windows API to set the desktop wallpaper.
6. If the operating system is Linux, it uses the `subprocess` module to run the `gsettings` command, which sets the desktop wallpaper for the GNOME desktop environment.
7. If the operating system is neither Windows nor Linux, it prints a message stating that the operating system is not supported.

In the main part of the script, it calls the `change_wallpaper()` function to change the desktop wallpaper.

## Dependencies

This script uses the following Python modules:

- `os`: A built-in module for interacting with the operating system.
- `random`: A built-in module for generating random numbers and making random choices.
- `platform`: A built-in module for retrieving information about the underlying platform.
- `ctypes` (Windows only): A built-in module for calling functions from shared libraries or DLLs.
- `subprocess` (Linux only): A built-in module for spawning new processes and running shell commands.

## Notes

- Make sure to replace `/path/to/your/dir` with the actual path to the directory containing your wallpaper images.
- The script assumes that all image files in the specified directory are valid and supported by your operating system.
- For Linux, the script is designed to work with the GNOME desktop environment. If you are using a different desktop environment, you may need to modify the `gsettings` command accordingly.
- This script only changes the desktop wallpaper. It does not provide any additional features for cycling through wallpapers or scheduling wallpaper changes.
