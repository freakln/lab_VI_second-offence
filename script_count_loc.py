import csv

from git import Repo

from count_loc import count_loc


headers = ['owner', 'name', 'url', 'stargazers', 'watchers', 'forkCount',
           'isFork', 'commitComments', 'releases', 'createdAt', 'primaryLanguage']

with open('retrabalho.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, fieldnames=['owner', 'name', 'url'], delimiter=';', quotechar='|')
    for row in spamreader:

        if row['name'] == 'name':
            continue
        try:
            loc = count_loc('repos/' + row['name'])
            print(row, loc)
        except:
            continue
