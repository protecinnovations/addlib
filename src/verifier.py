import os
import glob
from change import Change
#from addlib import Addlib

class Verifier(object):
    """
    Verifies and mends the working state of the changeset
    """
    def __init__(self):
        self.__change_dir = '/home/users/jez/changes'
        self.__changes = []
        self.__root = None

    def get_change_count(self):
        return len(self.__changes)

    def get_root(self):
        return self.__root
    
    def load_changeset(self):
        """
        Load in the entire changeset as an unordered list
        """
        del self.__changes[:]
        
        for file in glob.glob(os.path.join(self.__change_dir, '*.yaml')):
            self.__changes.append(Change(file))
            
    def check_working_state(self):
        """
        Check to see if the working state is valid, i.e. not a tree
        """
        self.load_changeset()
        # find the root
        root_candidates = self.find_dependencies_on(None)
        if len(root_candidates) > 1:
            # later we can probably resolve this problem...
            print 'You have the wrong number of base migrations:'

            for c in root_candidates:
                print self.describe_change(c) + ' (' + c.get_filename() + ')'
            exit(1)

        elif len(root_candidates) == 0:
            exit('Could not identify a base migration')
        else:
            self.__root = root_candidates[0];

        return self.check_for_dependents(self.__root)
            
    def check_for_dependents(self, change, and_resolve = False):
        """
        Have a look at a change and see if it is depended on by anything 
        """
        dependents_of_change = self.find_dependencies_on(change)

        if len(dependents_of_change) > 1:
            if and_resolve:
                print self.describe_change(change)
                self.solve_multiple_dependents(change, True)
            else:
                return False

        elif len(dependents_of_change) == 1:
            return self.check_for_dependents(dependents_of_change[0])
        else:
            # need to check that all changes have been checked - i.e. do we have a broken list?
            return True
      
    def solve_multiple_dependents(self, change, and_resolve = False):
        """
        Resolve situations where a change has more than one child
        """
        dependents_of_change = self.find_dependencies_on(change)
        
        if len(dependents_of_change) == 1:
            return
        
        print '...has the following dependents:\n'
        
        for i, a_change in enumerate(dependents_of_change):
            print str(i+1) + ':\n' + self.describe_change(a_change) + '\n'
            
        print 'Please nominate one migration to be the parent of the others...'
        number = int(raw_input('> '))
        
        nominated = dependents_of_change[number-1]
        
        for a_change in dependents_of_change:
            if a_change != nominated:
                a_change.set_depends_on(nominated)
                
                a_change.persist()
                
        self.check_for_dependents(nominated, and_resolve)
        
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
    