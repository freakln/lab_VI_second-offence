from git import Repo
from radon import raw,metrics
import os
import shutil


def clone_to_root(git_url, name):
    Repo.clone_from(git_url, 'repos/' + name)


# clone_to_root('https://github.com/gvanrossum/pegen','pegen')


print(metrics.analyze('.main.py'))


