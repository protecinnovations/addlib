#!/usr/bin/env python
from verifier import Verifier

class Addlib(object):

    verifier = Verifier()

    def __init__(self):
        pass
    
    @staticmethod
    def todo():
        """Get a list of changes that need to be applied
        """

    @staticmethod
    def status(then_exit = True):
        state = Addlib.verifier.check_working_state()
        print 'Working state has a total of ' + str(Addlib.verifier.get_change_count()) + ' migrations.'

        if state:
            print 'Congratulations! Working state is good.\n'
            if then_exit:
                exit(0)
        else:
            print 'Working state is bad. Run `addlib resolve` to fix this.\n'

            if then_exit:
                exit(1)

    @staticmethod
    def resolve():
        if Addlib.verifier.check_working_state():
            print 'Nothing to resolve.\n'
            Addlib.status()
        else:
            print 'Resolve working state...\n'
            Addlib.verifier.check_for_dependents(Addlib.verifier.get_root(), True)
            Addlib.status()
        

    @staticmethod
    def deploy():
        """Apply any waiting changes to the database
        """
        
    @staticmethod
    def undo(change_name):
        """Undo the specified change
        """
        print 'I haven\'t quite got around to implementing this yet.'
        