import sqlite3, sys
import logging
from cmd import Cmd


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
 
    def do_exit(self, inp):
        print("Bye")
        return True

    def do_cve(self, param):
        print(param)

    def help_cve(self):
        print("help_searcj")

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

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
 
    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    KennaSh().cmdloop()