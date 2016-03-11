from .base.workers import BaseTask

import os
import zipfile


class Unzip(BaseTask):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.target = kwargs.get('target')

    def description(self):
        return 'Extracting ' + self.source + ' to ' + self.target

    def prepare(self, **kwargs):
        self.source = kwargs.get('archive')

    def beforeExecute(self):
        if not os.path.exists(self.target):
            os.makedirs(self.target)

    def execute(self, **kwargs):
        with zipfile.ZipFile(self.source, "r") as z:
            z.extractall(self.target)

    def afterExecute(self):
        os.remove(self.source)
