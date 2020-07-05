import requests
import sys, os

kenna_api_key = ""
usage = "USAGE"

if len(sys.argv) != 2:
    print(sys.argv[1])
    if sys.argv[1] == '-i':
        print("HEHE")
    else:
        print(usage)
else:
    print(usage)