from .base.task import BaseTask

import os
import zipfile


class Unzip(BaseTask):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.target = kwargs.get('target')
        self.source = None

    def description(self, **args):
        source = args.get('archive', 'Unknown')
        return 'Extracting ' + source + ' to ' + self.target

    def beforeExecute(self):
        if not os.path.exists(self.target):
            os.makedirs(self.target)

    def doExecute(self, **kwargs):
        self.source = kwargs['archive']

        with zipfile.ZipFile(self.source, "r") as z:
            z.extractall(self.target)

    def afterExecute(self):
        os.remove(self.source)
