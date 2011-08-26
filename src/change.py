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
        self.__do_sql = parsed[root]['do']
        self.__undo_sql = parsed[root]['undo']
        self.__redo_sql = parsed[root]['redo']
        self.__depends_on_path = None

        if parsed[root]['depends'] != None:
            dependency_path = os.path.dirname(changefile) + '/' + parsed[root]['depends']
            self.__depends_on_path = dependency_path

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_do_sql(self):
        return self.__doSql

    def get_undo_sql(self):
        return self.__undoSql

    def get_redo_sql(self):
        return self.__redoSql

    def get_depends_on(self):
        if self.__dependsOnPath != None:
            return Change(self.__dependsOnPath)
        return None

    def set_depends_on(self, previous_change):
        """
        @previous_change Change
        Sets the change that this change depends on.
        """
        self.__dependsOn = previous_change
