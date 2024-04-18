#!/usr/bin/python3
"""cli for the Airbnb project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Class"""

    def __init__(self):
        """__init__ Method"""
        
        self.prompt = '(hbnb)'

    def do_EOF(self, line):
        """Method TO Handle EOF"""

        return true

    def do_quit(self, line):
        """Method TO Handle Quit Command"""

        return true




if __name__ == '__main__':
    HBNBCommand().cmdloop()
