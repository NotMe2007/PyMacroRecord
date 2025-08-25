# PyMacroRecord

[![pmr logo](https://github.com/LOUDO56/PyMacroRecord/assets/117168736/ff16ba4d-7979-4719-bb8f-78587cb5032f)](https://github.com/LOUDO56/PyMacroRecord/releases)

Coded with Python, PyMacroRecord is a free and easy macro recorder. No ads, no premium features — everything is free.

![Downloads](https://img.shields.io/github/downloads/LOUDO56/PyMacroRecord/total?label=Downloads)

## Overview

PyMacroRecord provides a GUI based on tkinter to record and replay mouse and keyboard actions.

## Features

- Easy to use
- Free, no premium features
- Infinite repeat
- Adjustable speed
- Interval / For / Schedule playback controls
- Save, load, and share macros
- After-playback options (standby, shutdown, etc.)
- Selective recording (mouse movement, clicks, keyboard)
- Custom hotkeys

## How it works

- Press the red button to start recording. Move the mouse, click, and type — the app records the events you enabled.
- Click the black square to stop recording.
- Click the green play icon to start playback. Press `F3` (default) to stop playback.

## Showcase

### Windows

![Windows showcase](https://github.com/LOUDO56/PyMacroRecord/assets/117168736/ac77b7b6-02d0-4c12-a71a-65119c4acc59)

### macOS

![macOS showcase](https://github.com/LOUDO56/PyMacroRecord/assets/117168736/2e8d8a85-c96b-4906-b8d9-b91de2c3d35b)

### Linux

![Linux showcase](https://github.com/LOUDO56/PyMacroRecord/assets/117168736/25ab7c60-9f48-425f-bd5f-68c8b76e4c9c)

- If you are on Linux you might need to install Tkinter via your package manager: see [Install Tkinter on Linux](https://www.geeksforgeeks.org/how-to-install-tkinter-on-linux/)
- On macOS, allow accessibility and input monitoring for the Terminal app.
- (Optional) Use a virtual environment; see [virtualenv guide](https://stackoverflow.com/a/41799834)

Run the app:

  cd src
  python3 main.py

## Build (Windows)

To build the application, I use PyInstaller.

You need to be on home directory, not on src.

Then, use that command for onefile output (upx is optional).

  pyinstaller --noconfirm --onefile --windowed --icon "src/assets/logo.ico" --name "PyMacroRecord-portable" --contents-directory "." --upx-dir upx --add-data "src/assets;assets/" --add-data "src/hotkeys;hotkeys/" --add-data "src/macro;macro/" --add-data "src/utils;utils/" --add-data "src/windows;windows/" --add-data "src/langs;langs"  "src/main.py"

For onedir output, use that command (upx is optional).

  pyinstaller --noconfirm --onedir --windowed --icon "src/assets/logo.ico" --name "PyMacroRecord" --contents-directory "." --upx-dir upx --add-data "src/assets;assets/" --add-data "src/hotkeys;hotkeys/" --add-data "src/macro;macro/" --add-data "src/utils;utils/" --add-data "src/langs;langs" --add-data "src/windows;windows/"  "src/main.py"

## Support

Developing software is not an easy task. If you like this project, please consider making a small donation — it helps a lot.

By donating, your name may appear in the "Donors" section of PyMacroRecord as a thank you.

[Buy me a coffee](https://ko-fi.com/loudo) ![ko-fi](https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0)

## License

This program is under [GNU General Public License v3.0](https://github.com/LOUDO56/PyMacroRecord/blob/main/LICENSE.md)

## Special Thanks

- Fooinys, who playtested the program.
- [Lenoch](https://github.com/Lenochxd), for code enhancement.
- [Takiem](https://github.com/takiem) for the Italian and Brazilian-Portuguese translation.
- [DennyClarkson](https://github.com/DennyClarkson) for the Chinese-Simplified translation.
- [SerdarSaglam](https://github.com/SerdarSaglam) for the Turkish translation.
- [superstes](https://github.com/superstes) for the German translation.
- [SqlWaldorf](https://github.com/SqlWaldorf) for the Dutch translation.
- [jorge-sepulveda](https://github.com/jorge-sepulveda) for the Spanish translation.
- [expp121](https://github.com/expp121) for the Bulgarian translation.
