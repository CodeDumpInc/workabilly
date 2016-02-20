from .base.workers import BaseWorker

import os
import shutil
import wget


class GithubArchiveGrabber(BaseWorker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = kwargs.get('user')
        self.project = kwargs.get('project')
        self.tag = kwargs.get('tag')
        self.branch = kwargs.get('branch', 'master')
        self.target = kwargs.get('target', './')

    def preExecuteDescription(self):
        return 'Creating Temporary Folder ' + self.target

    def postExecuteDescription(self):
        return 'Deleting Temporary Folder ' + self.target

    def executeDescription(self):
        return 'Downloading ' + self.project

    def _buildUrl(self):
        archive = self.tag
        if archive is None:
            archive = self.branch

        format_str = ("https://github.com/%s/%s/archive/%s.zip")
        return format_str % (self.user, self.project, archive)

    def preExecute(self):
        if not os.path.exists(self.target):
            os.makedirs(self.target)

    def execute(self, **kwargs):
        url = self._buildUrl()
        self.archive = wget.download(url, out=self.target)
        return {'archive': self.archive}

    def postExecute(self):
        shutil.rmtree(self.target)
