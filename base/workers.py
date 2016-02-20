

class BaseWorker:

    def __init__(self, **kwargs):
        self.next = None
        self.verbose = kwargs.get('verbose', True)

    def _printDescription(self, desc):
        if self.verbose:
            if desc:
                print(desc)

    def _printPreExecute(self):
        desc = self.preExecuteDescription()
        self._printDescription(desc)

    def _printExecute(self):
        desc = self.executeDescription()
        self._printDescription(desc)

    def _printPostExecute(self):
        desc = self.postExecuteDescription()
        self._printDescription(desc)

    def prepareWork(self, **kwargs):
        '''Override this to retrieve arguments before work starts'''

    def preExecuteDescription(self):
        pass

    def postExecuteDescription(self):
        pass

    def executeDescription(self):
        pass

    def preExecute(self):
        '''Gets called before the actual work is done'''

    def execute(self, **kwargs):
        '''Override this to do the deed'''

    def postExecute(self):
        '''Gets called after self and next are done'''