import yaml
import os

class Change(object):

    def __init__(self, changefile):
        # Parse the changefile and populate this object.
        f = open(changefile)
        parsed = yaml.load(f.read())
        f.close()
        root = parsed.keys()[0]

        self.__name = root
        self.__description = parsed[root]['description']
        self.__doSql = parsed[root]['do']
        self.__undoSql = parsed[root]['undo']
        self.__redoSql = parsed[root]['redo']
        self.__dependsOnPath = None

        if parsed[root]['depends'] != None:
            dependencyPath = os.path.dirname(changefile) + '/' + parsed[root]['depends']
            self.__dependsOnPath = dependencyPath

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getDoSql(self):
        return self.__doSql

    def getUndoSql(self):
        return self.__undoSql

    def getRedoSql(self):
        return self.__redoSql

    def getDependsOn(self):
        if self.__dependsOnPath != None:
            return Change(self.__dependsOnPath)
        return None

    def setDependsOn(self, previous_change):
        """
        @previous_change Change
        Sets the change that this change depends on.
        """
        self.__dependsOn = previous_change
