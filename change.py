class Change(object):

    def __init__(self, changefile):
        # Parse the changefile and populate this object.
        self.__name = ''
        self.__description = ''
        self.__doSql = ''
        self.__undoSql = ''
        self.__redoSql = ''
        self.__previousChange = ''

    def getName():
        return self.__name

    def getDescription():
        return self.__description

    def getDoSql():
        return self.__doSql

    def getUndoSql():
        return self.__undoSql

    def getRedoSql():
        return self.__redoSql

    def getPreviousChange():
        return self.__previousChange

    def setPreviousChange(previous_change):
        """
        @previous_change Change
        Sets the change that this change depends on.
        """
        self.__previousChange = previous_change
