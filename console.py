#!/usr/bin/python3
""" Module that contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state imoprt State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter

    Attributes:
    prompt (str): The command prompt
    """

    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        """ Command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Signal to exit the program """
        return True

    def emptyline(self):
        """ Take no action when an empty line is received """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}()")
            print(new_instance.id)

    def do_show(self, arg):
