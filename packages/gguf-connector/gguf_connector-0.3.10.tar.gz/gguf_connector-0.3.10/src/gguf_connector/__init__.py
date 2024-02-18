# !/usr/bin/env python3

__version__="0.3.10"

def __init__():
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
            with urllib.request.urlopen(url) as response, \
                open(filename, 'wb') as file, \
                tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc=f'Downloading {filename}') as pbar:
                chunk_size = 1024
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    file.write(chunk)
                    pbar.update(len(chunk))
            print(f"\nFile cloned successfully and saved as '{filename}' in the current directory.")
        except Exception as e:
            print(f"Error: {e}")

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", help="choose a subcommand")
    subparsers.add_parser('c', help='[c] gui connector c')
    subparsers.add_parser('cpp', help='[cpp] connector cpp')
    subparsers.add_parser('g', help='[g] cli connector g')
    subparsers.add_parser('gpp', help='[gpp] connector gpp')
    subparsers.add_parser('m', help='[m] connector selection menu')

    cc_parser = subparsers.add_parser('cc', help='[cc url] clone a GGUF file from URL as local copy')
    cc_parser.add_argument('url', type=str, help='URL to clone from')

    args = parser.parse_args()

    if args.subcommand == 'cc':
        clone_file(args.url)
    elif args.subcommand=="m":
        from gguf_connector import menu
    elif args.subcommand=="c":
        from gguf_connector import c
    elif args.subcommand=="cpp":
        from gguf_connector import cpp
    elif args.subcommand=="g":
        from gguf_connector import g
    elif args.subcommand=="gpp":
        from gguf_connector import gpp
