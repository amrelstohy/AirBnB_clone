#!/usr/bin/python3
"""
console module
"""

import cmd
from models import base_model
from models.engine import file_storage


class HBNBCommand(cmd.Cmd):

    """
    the class of console
    """
    prompt = '(hbnb)'
    __file_path = "file.json"

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """empty line function"""
        pass

    def do_create(self, *args):
        """creat new object"""

        if (args[0] == "BaseModel"):
            x = base_model.BaseModel()
            file_storage.FileStorage.save(self)
            print(x.id)
        elif (args[0] == ''):
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""

        a = 0
        args = line.split()
        if (len(args) == 0):
            print("** class name missing **")
        elif (len(args) == 1):
            if (args[0] == "BaseModel"):
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif (len(args) > 1):
            if (args[0] == "BaseModel"):
                x = file_storage.FileStorage.all(self)
                id = args[0] + '.' + args[1]
                for key, value in x.items():
                    if (key == id):
                        a = value
                if (a):
                    print(a)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        a = 0
        args = line.split()
        if (len(args) == 0):
            print("** class name missing **")
        elif (len(args) == 1):
            if (args[0] == "BaseModel"):
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif (len(args) > 1):
            if (args[0] == "BaseModel"):
                x = file_storage.FileStorage.all(self)
                id = args[0] + '.' + args[1]
                for key, value in x.items():
                    if (key == id):
                        a = value
                if (a):
                    x.pop(id)
                    file_storage.FileStorage.save(self)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances"""

        if (line == ''):
            x = file_storage.FileStorage.all(self)
            for key, value in x.items():
                print(value)
        elif (line == "BaseModel"):
            x = file_storage.FileStorage.all(self)
            for key, value in x.items():
                print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        args = line.split()
        len1 = len(args)
        if (len1 == 0):
            print("** class name missing **")
            return
        if (args[0] != "BaseModel"):
            print("** class doesn't exist **")
            return
        if (len1 == 1):
            print("** instance id missing **")
            return
        x = file_storage.FileStorage.all(self)
        key = args[0] + '.' + args[1]
        if (key not in x):
            print("** no instance found **")
            return
        if (len1 == 2):
            print("** attribute name missing **")
            return
        if (len1 == 3):
            print("** value missing **")
            return
        x[key].__dict__[args[2]] = args[3]
        x[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
