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
        self.__depends_on = None
        self.__filename = changefile

        if parsed[root]['depends'] != None:
            dependency_path = os.path.dirname(changefile) + '/' + parsed[root]['depends']
            self.__depends_on_path = dependency_path

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_do_sql(self):
        return self.__do_sql

    def get_undo_sql(self):
        return self.__undo_sql

    def get_redo_sql(self):
        return self.__redo_sql
    
    def get_filename(self):
        return self.__filename

    def get_depends_on(self):
        if self.__depends_on != None:
            return self.__depends_on
        elif self.__depends_on_path != None:
            return Change(self.__depends_on_path)
        
        return None
    
    def depends_on(self, change):
        if change == None and self.get_depends_on() == None:
            return True
        elif change == None or self.get_depends_on() == None:
            return False
        elif change.get_name() == self.get_depends_on().get_name():
            return True
        
        return False

    def set_depends_on(self, previous_change):
        """
        @previous_change Change
        Sets the change that this change depends on.
        """
        self.__depends_on = previous_change
    
    def persist(self):
        
        stream = file(self.get_filename(), 'w')
        
        output = """%s:
    description:    %s
    depends:        %s
    do: |
        %s
    undo: |
        %s
    redo: |
        %s
""" % (self.get_name(), self.get_description(), 
        os.path.basename(self.get_depends_on().get_filename()), self.get_do_sql().replace('\n', '\n        '),
        self.get_undo_sql().replace('\n', '\n        '), self.get_redo_sql().replace('\n', '\n        '))
        
        stream.write(output)
        stream.close()
        
