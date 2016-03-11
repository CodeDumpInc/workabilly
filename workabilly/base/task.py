

class BaseTask:

    def __init__(self, **kwargs):
        self.next = None
        self.verbose = kwargs.get('verbose', True)

    def run_necessary(self, **args):
        return True

    def describe(self, **args):
        if self.verbose:
            description = self.description(**args)
            if description:
                print(description)

    def execute(self, **args):
        if not self.run_necessary(**args):
            return

        result = self.doExecute(**args)
        if result is None:
            return {}

        return result

    def description(self, **args):
        '''Override this to print a description of the job'''

    def beforeExecute(self, **args):
        '''Gets called before the actual work is done'''

    def doExecute(self, **kwargs):
        '''Override this to do the deed'''

    def afterExecute(self):
        '''Gets called after self and next are done'''
