#!/usr/bin/env python3

import sys
import pathlib
import argparse
from os.path import isdir
from os.path import isfile
from os.path import expanduser

try:
    import dropbox
except Exception:
    print("\npip3 install dropbox\n")
    raise

HOME = expanduser("~")
TOKEN_DIR = f"{HOME}/tokens"
TARGET_DIR = f"{HOME}/storage/dropbox"
SECRET_TOKEN = f"{TOKEN_DIR}/.dropbox.token.secret"


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


def error(msg):
    pre = Color.RED + '!!!' + Color.END
    print(f"{pre} {msg}")


def list_all_files(dbx_auth, path):
    file_paths = dbx_auth.files_list_folder(path).entries
    for f in file_paths:
        if type(f) == dropbox.files.FolderMetadata:
            yield from list_all_files(dbx_auth, f.path_lower)
        elif type(f) == dropbox.files.FileMetadata:
            yield f.path_lower


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch files via DropBox API")
    parser.add_argument("-f", "--force",
                        action='store_true',
                        help="Force re-fetching of files.")
    parser.add_argument("-s", "--source",
                        metavar='PATH', default='',
                        help="Specify path in dropbox folder to fetch from.\
                              Default: ''")
    parser.add_argument("-d", "--destination",
                        metavar='PATH', default=TARGET_DIR,
                        help=f"Specify path to store fetched dropbox files to.\
                               Default: {TARGET_DIR}")
    parser.add_argument("-t", "--token",
                        metavar='PATH', default=SECRET_TOKEN,
                        help=f"Specify path to dropbox token.\
                               Default: {SECRET_TOKEN}")
    args = parser.parse_args()
    force_refetches = args.force
    source_dir = args.source
    destination_dir = args.destination
    token_path = args.token

    try:
        with open(token_path, 'r') as f:
            token = f.read().strip()
        dbx = dropbox.Dropbox(token)

        note("Fetching files from user's dropbox")
        if source_dir and not source_dir.startswith('/'):
            source_dir = '/' + source_dir
        for dropbox_file in list_all_files(dbx, source_dir):
            destination_file = destination_dir + dropbox_file
            destination_base = '/'.join(destination_file.split('/')[:-1])
            if not isdir(destination_base):
                pathlib.Path(destination_base).mkdir(parents=True)
                alert(f"Created dir {destination_base}")
            if not isfile(destination_file) or force_refetches:
                dbx.files_download_to_file(destination_file, dropbox_file)
                checkmark(f"{destination_file}")
            else:
                alert(f"Already exists: {destination_file}")
        note("Script finished!")
        checkmark(destination_dir)
    except dropbox.exceptions.BadInputError as e:
        error(f"Error with parsing token.\
                Check if tokenfile is correctly set: {token_path}")
        error(e)
        sys.exit(1)
    except dropbox.exceptions.ApiError as e:
        error(f"Error with API call.\
                Check if this dropbox directory exists: {source_dir}")
        error(e)
        sys.exit(1)
    except Exception as e:
        error("General exception occurred")
        error(e)
        raise
