#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class definition for holberton AirBnB console """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit from console """
        exit()

    def do_EOF(self, arg):
        """ Handle method to exit when EOF """
        print()
        exit()

    def emptyline(self):
        """ Method to print the prompt again when emptyline entered """
        pass

    def do_create(self, args):
        """ Command to create a new instance of class BaseModel and
        saves it to the JSON file. """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

        except:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
