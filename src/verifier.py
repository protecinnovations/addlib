import os
import glob
from change import Change
from addlib import Addlib

class Verifier(object):
    """
    Verifies and mends the working state of the changeset
    """
    def __init__(self):
        self.__change_dir = '/home/users/jez/changes'
        self.__changes = []
    
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
        print '\nChecking change:\n' + Addlib.describe_change(change)
            
        dependents_of_change = self.find_dependencies_on(change)

        if len(dependents_of_change) > 1:
            self.solve_multiple_dependents(change)
        elif len(dependents_of_change) == 1:
            print '...which has one dependent change, called "' + dependents_of_change[0].get_name() + '".'
            self.check_for_dependents(dependents_of_change[0])
        else:
            print '...which has no dependent changes.'
            # need to check that all changes have been checked - i.e. do we have a broken list?
      
    def solve_multiple_dependents(self, change):
        """
        Resolve situations where a change has more than one child
        """
        dependents_of_change = self.find_dependencies_on(change)
        
        if len(dependents_of_change) == 1:
            return
        
        print '...has the following dependents:\n'
        
        for i, a_change in enumerate(dependents_of_change):
            print str(i+1) + ':\n' + Addlib.describe_change(a_change) + '\n'
            
        print 'Please nominate a change to be the parent of the others...'
        number = int(raw_input('> '))
        
        nominated = dependents_of_change[number-1]
        
        for a_change in dependents_of_change:
            if a_change != nominated:
                a_change.set_depends_on(nominated)
                
                a_change.persist()
                
        self.check_for_dependents(nominated)
        
    def find_dependencies_on(self, change):
        """
        Find all the changes that depend on the given change
        """
        changes = []
        for a_change in self.__changes:
            if a_change.depends_on(change):
                changes.append(a_change)
        
        return changes
    
me = Verifier()
    
me.check_working_state()