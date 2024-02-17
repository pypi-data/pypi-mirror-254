# !/usr/bin/env python3

__version__="0.3.9"

def __init__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    # parser.add_argument("connector", help="choose a connector: c, cpp, g, gpp; or m (menu)")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", help="Choose a subcommand")
    subparsers.add_parser('c', help='[c] gui connector c')
    subparsers.add_parser('cpp', help='[cpp] connector cpp')
    subparsers.add_parser('g', help='[g] cli connector g')
    subparsers.add_parser('gpp', help='[gpp] connector gpp')
    subparsers.add_parser('m', help='[m] connector selection menu')
    args = parser.parse_args()

    if args.subcommand=="m":
        from gguf_connector import menu
    elif args.subcommand=="c":
        from gguf_connector import c
    elif args.subcommand=="cpp":
        from gguf_connector import cpp
    elif args.subcommand=="g":
        from gguf_connector import g
    elif args.subcommand=="gpp":
        from gguf_connector import gpp
        
    # if args.connector=="m":
    #     from gguf_connector import menu
    # if args.connector=="c":
    #     from gguf_connector import c
    # elif args.connector=="cpp":
    #     from gguf_connector import cpp
    # elif args.connector=="g":
    #     from gguf_connector import g
    # elif args.connector=="gpp":
    #     from gguf_connector import gpp
    # print("in __init__ function")