#!/usr/bin/python3
"""cli for the Airbnb project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Class"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Method TO Handle EOF"""

        return True

    def do_quit(self, line):
        """Method TO Handle Quit Command"""

        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
