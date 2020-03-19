import csv
import time
import requests
from query import query
inicio = time.time()
names = []
to_csv = []

after = ''
headers = {"Authorization": "token 324716e91612c5d9c98edc464cb4581c70a7bd86"}

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

        nodes += result['data']['search']['nodes']

        have_next_page = result["data"]["search"]["pageInfo"]["hasNextPage"]
        page += 1
        print(result["data"]["search"]["pageInfo"]["endCursor"])
        after = ', after:"' + result["data"]["search"]["pageInfo"]["endCursor"]+'"'
        mquery = query % after


for d in nodes:
    row = {}
    for keys in d.keys():
        if keys not in names:
            names.append(keys)
        row.update({keys: d[keys]})
    to_csv.append(row)

with open('resultado.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=names, delimiter=';')
    writer.writeheader()
    for i in to_csv:
        writer.writerow(i)

print(time.time() - inicio)
