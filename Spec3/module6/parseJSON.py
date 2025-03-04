import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
js = json.loads(data)

comments = js['comments']
counts = list()
for comment in comments:
    counts.append(comment['count'])
print('Total comments:', sum(counts))