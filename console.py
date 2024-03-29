"""
console module
"""

import cmd
import re
from models.base_model import BaseModel
from models.engine import file_storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    the class of console
    """

    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}
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

    def do_create(self, line):
        """creat new object"""

        args = line.split()
        len_line = len(args)
        if (len_line == 0):
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
            return
        x = HBNBCommand.classes[args[0]]()
        print(x.id)
        if (len_line == 1):
            return
        for attr in args[1:]:
            param = attr.split("=")
            if (len(param) != 2):
                return
            if (param[1].isnumeric()):
                x.__dict__[param[0]] = int(param[1])
            elif(re.match(r'^[0-9]+\.[0-9]+$',param[1]) is not None):
                x.__dict__[param[0]] = float(param[1])
            elif (param[1][0] == '"' and param[1][-1] == '"'):
                param[1] = param[1].replace('_', ' ')
                param[1] = param[1][1:-1]
                x.__dict__[param[0]] = param[1]
        file_storage.FileStorage.save(self)

    def do_show(self, line):
        """Prints the string representation of an instance"""

        args = line.split()
        len1 = len(args)

        if (len1 == 0):
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
            return
        if (len1 == 1):
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objs = file_storage.FileStorage.all(self)
        if (key not in objs):
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        args = line.split()
        len1 = len(args)

        if (len1 == 0):
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
            return
        if (len1 == 1):
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objs = file_storage.FileStorage.all(self)
        if (key not in objs):
            print("** no instance found **")
            return
        objs.pop(key)
        file_storage.FileStorage.save(self)

    def do_all(self, line):
        """Prints all string representation of all instances"""

        if (line == '' or line in HBNBCommand.classes):
            x = file_storage.FileStorage.all(self)
            for key, value in x.items():
                print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        args = line.split()
        len1 = len(args)
        if (len1 == 0):
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.classes):
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
