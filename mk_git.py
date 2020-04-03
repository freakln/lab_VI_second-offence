import math
import os
from git import Repo
from radon.raw import analyze
import pathlib
import shutil
import csv
import time
import requests
import json
from count_loc import count_loc

inicio = time.time()
time.sleep(7)

loc = []
headers = ['owner', 'name', 'url', 'stargazers', 'watchers', 'forkCount',
           'isFork', 'commitComments', 'releases', 'createdAt', 'primaryLanguage']

with open('retrabalho.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, fieldnames=['owner', 'name'], delimiter=';', quotechar='|')
    for row in spamreader:
        print(row)
        if row['name'] == 'name':
            continue
        try:
            print(row['owner'], row['name'])
            success = False
            while not success:
                tempo = time.time()
                response = requests.get(
                    'https://api.codetabs.com/v1/loc?github={}/{}'.format(row['owner'], row['name']))
                print(response.status_code)
                if response.status_code == 429:
                    time.sleep(6)
                    success = False
                else:
                    for r in response.json():
                        if r['language'] == 'Total':
                            loc.append({'name': row['name'], 'loc': r['linesOfCode'], 'tempo':math.ceil(time.time() - inicio)})
                            success = True

        except:
            loc.append({'name': row['name'], 'loc': 'FAIL'})
            continue
csvfile.close()

with open('novoTeste.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['name', 'loc','tempo'], delimiter=';')
    writer.writeheader()
    for i in loc:
        writer.writerow(i)
print(math.ceil(time.time() - inicio))
