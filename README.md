# Workabilly

## What's this?

When checking out a project, you usually have to initialize some environment. This here is a proof-of-concept (or a mere attempt at one) for a task-based framework that gets such an environment set up. 

It is (or, will be) written with C++ in mind, where there is no single source for packages, and dependencies have to be compiled from various sources. 

## Installation

It's on PyPi, so just use:

`pip install workabilly`

## Usage

For now, there's a queue that is filled with workers. The queue is consumed item by item (queue, eh?) until there are no more tasks. 

This example downloads a specific googletest release and unzips it into a target folder.  

    from workabilly.archives import Unzipper
    from workabilly.github import GithubArchiveGrabber
    from workabilly.queue import WorkingQueue

    github_config = {
      'user': 'google',
      'project': 'googletest',
      'tag': 'release-1.7.0',
      'target': 'Temp'
    }
  
    queue = WorkingQueue()
    queue.add(GithubArchiveGrabber(**github_config))
    queue.add(Unzipper(target='ext'))
  
    queue.start()
