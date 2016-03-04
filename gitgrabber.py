from workabilly.archives import Unzipper
from workabilly.github import GithubArchiveGrabber
from workabilly.queue import WorkingQueue

if __name__ == '__main__':

    targets = [
        {
            'user': 'google',
            'project': 'googletest',
            'tag': 'release-1.7.0',
            'target': 'Temp'
        },
        {
            'user': 'google',
            'project': 'googlemock',
            'tag': 'release-1.7.0',
            'target': 'Temp'
        }
    ]

    workers = []

    for target in targets:
        queue = WorkingQueue()
        queue.add(GithubArchiveGrabber(**target))
        queue.add(Unzipper(target='ext'))

        workers.append(queue)

    for worker in workers:
        worker.start()
