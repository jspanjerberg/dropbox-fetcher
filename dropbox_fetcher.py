#!/usr/bin/env python3

import pathlib
from os.path import isdir
from os.path import isfile
from os.path import expanduser

try:
    import dropbox
except Exception:
    print()
    print("pip3 install dropbox")
    print()
    raise

HOME = expanduser("~")
TOKEN_DIR = f"{HOME}/tokens"
SECRET_FILENAME = f"{TOKEN_DIR}/.dropbox.secret"
TARGET_DIR = f"{HOME}/storage/dropbox"


class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    END = '\033[0m'


def note(msg):
    pre = Color.YELLOW + '>>>' + Color.END
    print(f"{pre} {msg}")


def checkmark(msg):
    pre = Color.GREEN + ' ✓ ' + Color.END
    print(f"{pre} {msg}")


def alert(msg):
    pre = Color.MAGENTA + ' ! ' + Color.END
    print(f"{pre} {msg}")


def list_all_files(dbx_auth, path):
    file_paths = dbx_auth.files_list_folder(path).entries
    for f in file_paths:
        if type(f) == dropbox.files.FolderMetadata:
            yield from list_all_files(dbx_auth, f.path_lower)
        elif type(f) == dropbox.files.FileMetadata:
            yield f.path_lower


if __name__ == "__main__":
    with open(SECRET_FILENAME, 'r') as f:
        TOKEN = f.read().strip()
    dbx = dropbox.Dropbox(TOKEN)

    note("Fetching files from dropbox")
    for dropbox_file in list_all_files(dbx, ''):
        destination_file = TARGET_DIR + dropbox_file
        destination_dir = '/'.join(destination_file.split('/')[:-1])
        if not isdir(destination_dir):
            pathlib.Path(destination_dir).mkdir(parents=True)
            alert(f"Created dir {destination_dir}")
        if not isfile(destination_file):
            dbx.files_download_to_file(destination_file, dropbox_file)
            checkmark(f"{destination_file}")
        else:
            alert(f"Already exists: {destination_file}")
