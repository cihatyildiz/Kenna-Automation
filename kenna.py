from cmd import Cmd
 
class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"
 
    def do_exit(self, inp):
        print("Bye")
        return True
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
 
    def do_add(self, inp):
        print("adding '{}'".format(inp))
 
    def help_add(self):
        print("Add a new entry to the system.")

    def do_connectors(self):
        print("do connectors")

    def help_connectors(self):
        print("help_connectors")

    def do_users(self):
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
    MyPrompt().cmdloop()