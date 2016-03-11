from .download import Download

import shutil


class GithubArchiveDownload(Download):

    def _buildUrl(self):
        archive = self.tag
        if archive is None:
            archive = self.branch

        format_str = ("https://github.com/%s/%s/archive/%s.zip")
        return format_str % (self.user, self.project, archive)

    def __init__(self, **kwargs):
        self.user = kwargs.get('user')
        self.project = kwargs.get('project')
        self.tag = kwargs.get('tag')
        self.branch = kwargs.get('branch', 'master')
        self.target = kwargs.get('target', './')

        super().__init__(source=self._buildUrl(), target=self.target)

    def description(self):
        return 'Downloading ' + self.project

    def doExecute(self, **kwargs):
        return {'archive': super().doExecute(**kwargs).get('downloaded')}

    def afterExecute(self):
        shutil.rmtree(self.target)
