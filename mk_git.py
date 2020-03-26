import os
from git import Repo
from radon.raw import analyze
import pathlib
import shutil
import csv
from teste import count_loc
headers = ['name', 'url', 'stargazers', 'watchers', 'forkCount',
           'isFork', 'commitComments', 'releases', 'createdAt', 'primaryLanguage']

with open('resultado.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, fieldnames=headers, delimiter=';', quotechar='|')
    for row in spamreader:
        if row['url'] == 'url':
            continue
        try:
            Repo.clone_from(row['url'],'repos/'+row['name'])
            count_loc('repos/'+row['name'])
        except:
            raise
