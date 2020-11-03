#!/usr/bin/python3
""" Import Modules
    Hint ---> list of libraries code to be use
"""
import cmd
from models.base_model import BaseModel
#from models import storage
#from models.user import User
#from models.state import State
#from models.city import City
#from models.place import Place
#from models.amenity import Amenity
#from models.review import Review
#import aux_functions

class HBNBCommand(cmd.Cmd):
    """ Command line main module """
    classes_list = ['BaseModel', 'User', 'City',
                    'State', 'Place', 'Amenity', 'Review']
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit coomand line
        Usage: 1 - quit 
        """
        return True
 
    def emptyline(self):
        " Empty Line "
        pass

    def do_EOF(self, args):
        """ EOF - press C^d to quit commnad line """
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()