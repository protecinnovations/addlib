
class MySQL(object):
    """
    Handles applying changesets to a MySQL database
    """
    
    def __init__(self, hostname, username, password, database):
        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__database = database
        
    def execute(self, changes):

        # start transaction

        for change in changes:
            log_sql = ('INSERT INTO `addlib_log` SET `change_name`="%s", `action`="%s", ' +
                'timestamp=%s, was_redo=%s;' % (change.get_name(), 'DO', time, 0))
            


    def head(self):
        """
        Returns the most recent change that has been applied.
        """
        pass
    