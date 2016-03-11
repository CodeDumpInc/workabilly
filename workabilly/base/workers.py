

class BaseTask:

    def __init__(self, **kwargs):
        self.next = None
        self.verbose = kwargs.get('verbose', True)

    def describe(self):
        if self.verbose:
            description = self.description()
            if description:
                print(description)

    def prepare(self, **kwargs):
        '''Override this to retrieve arguments before work starts'''

    def description(self):
        '''Override this to print a description of the job'''

    def beforeExecute(self):
        '''Gets called before the actual work is done'''

    def execute(self, **kwargs):
        '''Override this to do the deed'''

    def afterExecute(self):
        '''Gets called after self and next are done'''
