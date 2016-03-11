from .base.task import BaseTask

import os
import wget


class Download(BaseTask):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = kwargs.get('source')
        self.target = kwargs.get('target', './')

    def beforeExecute(self):
        if not os.path.exists(self.target):
            os.makedirs(self.target)

    def doExecute(self, **kwargs):
        result = wget.download(self.source, out=self.target)
        print("")
        return {'downloaded': result}
