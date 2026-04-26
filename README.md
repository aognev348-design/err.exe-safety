err.exe
This repository contains a Python script that uses the Windows GDI (Graphics Device Interface) to create visual screen effects. It is a safe demonstration of WinAPI capabilities, mimicking the aesthetic of classic malware for artistic purposes.
Warning
The script generates intense flashing lights and rapid color inversions. It is not suitable for individuals with photosensitive epilepsy.
Overview
The program performs direct drawing on the screen buffer. It does not modify files, registry keys, or system settings. All effects are temporary and will disappear once the process is terminated.
Features
 * Recursive screen stretching and tunneling effects.
 * Vertical falling "err.exe" text using a custom-stretched Arial font.
 * Floating RGB-cycle ellipse with bouncing physics.
 * Full-screen color XOR inversion using PATINVERT logic.
 * Random screen slicing and horizontal glitching.
   Requirements
 * Windows OS
 * Python 3.x
 * Administrative privileges (recommended for full screen access)
   Usage
Run the script via command line:
python main.py
To stop the execution and refresh the screen, press CTRL+C. The script calls InvalidateRect on exit to restore the desktop appearance.
 Technical details
The implementation relies on ctypes to interface with user32.dll and gdi32.dll. Core functions used include BitBlt, StretchBlt, and PatBlt for fast pixel manipulation without external dependencies.
