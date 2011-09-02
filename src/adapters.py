
class MySQL(object):
    """
    Handles applying changesets to a MySQL database
    """
    
    def __init__(self, hostname, username, password, database):
        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__database = database
        
    def execute(self, script):
        pass
        
    def head(self):
        pass