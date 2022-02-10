import os
import sys

def file_path(filename_pattern: str):
    treeroot = os.path.abspath(".")
    if hasattr(sys, '_MEIPASS'): # Used for pyinstaller bundling
        treeroot = sys._MEIPASS
    for directory_path, _, files in os.walk(treeroot):
        for filename in files:
            if filename_pattern in filename:
                return os.path.join(directory_path, filename)
    return ""
