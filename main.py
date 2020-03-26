import csv
import time
import requests
from query import query
inicio = time.time()
names = []
to_csv = []

after = ''

dado = ''
cursor = ''
have_next_page = True
page = 0

mquery = query % after
print(mquery)
nodes = list()
while have_next_page and page < 100:

    request = requests.post('https://api.github.com/graphql', json={'query': mquery}, headers=headers)
    print('page:' + str(page))
    print(request.status_code)
    if request.status_code == 200:
        result = request.json()
        print(result)
        nodes += result['data']['user']['repositories']['nodes']

        have_next_page = result["data"]["user"]['repositories']["pageInfo"]["hasNextPage"]
        page += 1
        print(result["data"]["user"]['repositories']["pageInfo"]["endCursor"])
        after = ', after:"' + result["data"]["user"]['repositories']["pageInfo"]["endCursor"]+'"'
        mquery = query % after


for d in nodes:
    row = {}
    for keys in d.keys():
        if keys not in names:
            names.append(keys)
        row.update({keys: d[keys]})
    to_csv.append(row)

with open('resul_tado.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=names, delimiter=';')
    writer.writeheader()
    for i in to_csv:
        writer.writerow(i)

print(time.time() - inicio)
