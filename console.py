#!/usr/bin/python3
"""
console module
"""
import cmd


class HBNBCommand(cmd.Cmd):

    """
    the class of console
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """empty line function"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
