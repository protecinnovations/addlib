import os
import glob
from change import Change

class Addlib(object):

    def __init__(self):
        self.__hostname = 'localhost'
        self.__username = 'root'
        self.__password = 'password'
        self.__database = 'phasefour'    
        self.__change_dir = '/home/users/jez/changes'
        self.__changes = []

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
    
    def load_changeset(self):
        """
        Load in the entire changeset as an unordered list
        """
        for file in glob.glob(os.path.join(self.__change_dir, '*.yaml')):
            self.__changes.append(Change(file))
            
    def check_working_state(self):
        """
        Check to see if the working state is valid, i.e. not a tree
        """
        self.load_changeset()
        # find the root
        root_candidates = self.find_dependencies_on(None)
        if len(root_candidates) > 1 or len(root_candidates) == 0:
            # later we can probably resolve this problem...
            exit('You have the wrong number of base changes')
        else:
            root = root_candidates[0];

        self.check_for_dependents(root)
            
    def check_for_dependents(self, change):
        """
        Have a look at a change and see if it is depended on by anything 
        """
        print 'Checking change:\n' + self.describe_change(change)
            
        dependents_of_change = self.find_dependencies_on(change)

        if len(dependents_of_change) > 1:
            print '...which has more than one dependent change!'
            # solve the problem....
            exit()
        elif len(dependents_of_change) == 1:
            print '...which has one dependent change, called "' + dependents_of_change[0].get_name() + '"'
        else:
            print '...which has no dependent changes, so I\'m stopping.'
            # need to check that all changes have been checked - i.e. do we have a broken list?
        
    def find_dependencies_on(self, change):
        """
        Find all the changes that depend on the given change
        """
        changes = []
        for a_change in self.__changes:
            if a_change.depends_on(change):
                changes.append(a_change)
        
        return changes
            
    def describe_change(self, change):
        return change.get_name() + '\t\t' + change.get_description()

me = Addlib()
me.check_working_state()

print '\n'