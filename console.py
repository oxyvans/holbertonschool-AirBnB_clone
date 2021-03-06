#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """

import cmd
import models
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


clases = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
          "Place": Place, "Review": Review, "State": State, "User": User}


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

    def do_create(self, command):
        """ Method to create  the class """
        if len(command) == 0:
            print("** class name missing **")
        elif command not in clases:
            print("** class doesn't exist **")
        else:
            for key, clas in clases.items():
                if command == key:
                    obj = clas()
                    obj.save()
                    print(obj.id)

    def do_show(self, command):
        """ Prints the string representation of an instance """
        cmd = command.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in clases:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            inst = cmd[0] + "." + cmd[1]
            if str(inst) in models.storage.all():
                print(models.storage.all()[inst])
            else:
                print("** no instance found **")

    def do_destroy(self, command):
        """ Deletes an instance based on the class name """
        cmd = command.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in clases:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            inst = cmd[0] + "." + cmd[1]
            if str(inst) in models.storage.all():
                models.storage.all().pop(inst)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, command):
        """ Prints all string representation of all instances based or not
        on the class name """
        res = []
        dic = models.storage.all()
        if len(command) == 0:
            for key in dic:
                res.append(dic[key].__str__())
            print(res)
        else:
            if command in clases:
                for key in dic:
                    if dic[key].__class__.__name__ == command:
                        res.append(dic[key].__str__())
                print(res)
            else:
                print("** class doesn't exist **")

    def do_update(self, command):
        """  Updates an instance based on the class name and id
        Usage: update <className> <id> <attName> <attVal> """
        cmd = command.split()
        objs = models.storage.all()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in clases:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        elif len(cmd) < 3:
            print("** attribute name missing **")
        elif len(cmd) < 4:
            print("** value missing **")
        else:
            inst = str(cmd[0] + "." + cmd[1])
            if inst in objs:
                objs[inst].__dict__[cmd[2]] = cmd[3].replace("\"", "")
                models.storage.save()
            else:
                print("** no instance found **")

    def do_count(self, command):
        """  number of instances of a class """
        if command in clases:
            cont = 0
            dic = models.storage.all()
            for v in dic.values():
                if command == v.__class__.__name__:
                    cont = cont + 1
            print(cont)
        else:
            print("** class doesn't exist **")

    def default(self, command):
        """ task 11 and 12"""
        cmd = command.split(".")
        if cmd[0] in clases and cmd[1] == "all()":
            HBNBCommand.do_all(self, cmd[0])
        elif cmd[0] in clases and cmd[1] == "count()":
            HBNBCommand.do_count(self, cmd[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
