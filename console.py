#!/usr/bin/python3
"""
This module contains the HBNBCommand class that implements
the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that implements the command interpreter.

    args:
    prompt: str that will be showed to the user

    Methods:
        do_quit(self, arg): Quit command to exit the program
        do_EOF(self, arg): Quit command to exit the program when receive EOF
        emptyline(self): Empty line + ENTER shouldn't execute anything
        help_quit(self): Help message for the quit command
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything
        """
        pass

    def help_quit(self):
        """
        Help message for the quit command
        """
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
