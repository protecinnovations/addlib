class Addlib(object):

    def __init__(self):
        self.__hostname = 'localhost'
        self.__username = 'root'
        self.__password = 'password'
        self.__database = 'phasefour'    
        self.__change_dir = '/home/users/jez/changes'

    def get_next_changes():
        """Get a list of changes that need to be applied
        """

    def deploy():
        """Apply any waiting changes to the database
        """

    def undo(change_name):
        """Undo the specified change
        """

    def get_dependencies(change_name):
        """Get a list of changes that depend on the given change
        """

