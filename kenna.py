#!/usr/bin/python3

import sys, os
import argparse



if __name__ == "__main__":

    # parse the arguments 
    parser = argparse.ArgumentParser(
        prog="kenna",
        description="Simple Tool for Kenna Security Platform",
        epilog="This tool uses kenna api platform to get information")

    parser.add_argument("search_pattern", metavar="search", type=str, help="Search pattern")
    parser.add_argument("-v", "--vulns", metavar="", help="get vulnerabilities based on search pattern")
    parser.add_argument("-a", "--assets", metavar="", help="get assets based on search pattern")
    parser.add_argument("-f", "--fixes", metavar="", help="get fixes based on search pattern")

    args = parser.parse_args()
    print(args.accumulate())
    print(args)
