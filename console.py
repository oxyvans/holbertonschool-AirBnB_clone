#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
