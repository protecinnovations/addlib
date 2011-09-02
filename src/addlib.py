class Addlib(object):

    def __init__(self):
        pass
    
    @staticmethod
    def get_next_changes():
        """Get a list of changes that need to be applied
        """
    
    @staticmethod
    def deploy():
        """Apply any waiting changes to the database
        """
        
    @staticmethod
    def undo(change_name):
        """Undo the specified change
        """
        
    @staticmethod
    def get_dependencies(change_name):
        """Get a list of changes that depend on the given change
        """
        
    @staticmethod
    def describe_change(change):
        return change.get_name() + '\t\t' + change.get_description()
    