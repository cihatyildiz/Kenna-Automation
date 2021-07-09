import sqlite3, sys
import logging
from cmd import Cmd
import re
import yaml

from lib.kenna import *

xintro = """
Delta Dental of California
██╗  ██╗███████╗███╗   ██╗███╗   ██╗ █████╗ 
██║ ██╔╝██╔════╝████╗  ██║████╗  ██║██╔══██╗
█████╔╝ █████╗  ██╔██╗ ██║██╔██╗ ██║███████║
██╔═██╗ ██╔══╝  ██║╚██╗██║██║╚██╗██║██╔══██║
██║  ██╗███████╗██║ ╚████║██║ ╚████║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝
Interactive Shell
"""

class KennaSh(Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = 'kenna> '
        self.intro = xintro
        self.kenna_api_key = ""
 
    def do_exit(self, inp):
        print("Bye")
        return True

    def do_cve(self, param):
        if param == "":
            print("Please specify a CVE number...")
        else:
            if verifyCveNumber(param):
                o_kenna = Kenna(self.kenna_api_key)
                asset_count = o_kenna.getAssetCountByCVE(param)
                print("There are {} vulnerable assets for {}".format(asset_count, param))
            else:
                print("Please specify a valid CVE number...")

    def help_cve(self):
        msg = "cve - shows vulnerable asset and vulnerability informaiton as high level\nUsage:\n\t cve <cve-number>"
        print(msg)

    def do_search(self, param):
        print("do_searcj")

    def help_search(self):
        print("help_searcj")

    def do_tickets(self, param):
        print("do_tickets")
    
    def help_tickets(self):
        print("help_tickets")

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
 
    def do_add(self, inp):
        print("adding '{}'".format(inp))
 
    def help_add(self):
        print("Add a new entry to the system.")

    def do_connectors(self, param):
        print("do connectors")

    def help_connectors(self, param):
        print("help_connectors")

    def do_users(self, param):
        print("help_users")
    
    def help_users(self):
        print("help_users")

    def emptyline(self):
        pass

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
 
    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':

    KennaSh().cmdloop()