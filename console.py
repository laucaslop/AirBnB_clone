#!/usr/bin/python3
""" Import Modules
    Hint ---> list of libraries code to be use
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
#import aux_functions


class HBNBCommand(cmd.Cmd):
    """ Command line main module """
    classes_list = ['BaseModel', 'User', 'City',
                    'State', 'Place', 'Amenity', 'Review']
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit coomand line
        Usage:
        1 - quit
        """
        return True

    def emptyline(self):
        " Empty Line "
        pass

    def do_EOF(self, args):
        """ EOF - press C^d to quit commnad line """
        print("")
        return True

    def do_create(self, args):
        """ Create a new instance
        Usage:
        1 - create <class name>
        """
        if len(args) < 1:
            print("** class name missing **")
        elif args not in self.classes_list:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        """ show an instance.
        Usage:
        1 - show <class> <id>
        2 - <class name>.show("<id>")
        """
        commands = args.split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in self. classes_list:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            key_validation = "{}.{}".format(commands[0], commands[1])
            if key_validation not in storage.all():
                print("** no instance found **")
            else:
                for key, obj in storage.all().item():
                    if key == key_validation:
                        print(obj)

    def do_destroy(self, args):
        """ Destroy an instance.
        Usage:
        1 - destroy <class> <id>
        2 - <class name>.destroy("<id>")
        """
        commands = args.split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in self. classes_list:
            print("** class doesn't exist **")
        elif command < 2:
            print("** instance id missing **")
        else:
            key_validation = "{}.{}".format(commands[0], commands[1])
            instances = storage.all()
            if key_to_validate not in instances:
                print("** no instance found **")
            else:
                del instances[key_to_validate]
                storage.save()

    def do_all(self, args):
        """ Print all instances.
        Usage:
        1 - all <class name>
        2 - all
        3 - <class name>.all()
        """
        if args not in self.classes_list and len(args) > 0:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            list_instances = []
            for key_id in instances.keys():
                key = key_id.split('.')
                if len(args) < 1:
                    list_instances.append(str(instances[key_id]))
                elif key[0] == args:
                    list_instances.append(str(instances[key_id]))
            print(list_instances)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
