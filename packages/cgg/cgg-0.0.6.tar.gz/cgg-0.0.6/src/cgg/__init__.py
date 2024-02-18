# !/usr/bin/env python3

__version__="0.0.6"

import argparse
import urllib.request
from os.path import basename
from tqdm import tqdm

def get_file_size(url):
    with urllib.request.urlopen(url) as response:
        size = int(response.headers['Content-Length'])
    return size

def clone_file(url):
    try:
        file_size = get_file_size(url)
        filename = basename(url)
        # Download the file with progress
        with urllib.request.urlopen(url) as response, \
             open(filename, 'wb') as file, \
             tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc=f'Downloading {filename}') as pbar:
            # Download in chunks and update the progress bar
            chunk_size = 1024  # 1 KB
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                file.write(chunk)
                pbar.update(len(chunk))
        print(f"\nFile cloned successfully and saved as '{filename}' in the current directory.")
    except Exception as e:
        print(f"Error: {e}")

def __init__():
    parser = argparse.ArgumentParser(description="cgg will execute different functions based on command-line arguments")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", help="choose a subcommand:")
    # Subparser for the 'clone + URL' command
    clone_parser = subparsers.add_parser('clone', help='download a GGUF file/model from URL')
    clone_parser.add_argument('url', type=str, help='URL to download from (i.e., egg clone [url])')
    # Subparser for the 'menu/cpp/c/gpp/g' command
    subparsers.add_parser('menu', help='connector selection list:')
    subparsers.add_parser('cpp', help='cpp connector')
    subparsers.add_parser('gpp', help='gpp connector')
    subparsers.add_parser('c', help='c connector')
    subparsers.add_parser('g', help='g connector')
    args = parser.parse_args()

    if args.subcommand == 'clone':
        clone_file(args.url)
    elif args.subcommand == 'menu':
        from gguf_connector import menu
    elif args.subcommand == 'cpp':
        from gguf_connector import cpp
    elif args.subcommand == 'c':
        from gguf_connector import c
    elif args.subcommand == 'gpp':
        from gguf_connector import gpp
    elif args.subcommand == 'g':
        from gguf_connector import g
