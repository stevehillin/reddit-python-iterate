import json
import requests

subreddits = ['automation']

keywords = ['python', 'automation', 'scrape', 'automate']

headers = {"User-agent": "aws:com.sample:v0.1.4 by /u/someone"}

for sub in subreddits:
    url = 'https://www.reddit.com/r/' + sub + '/new.json'
    result = requests.get(url, headers = headers)
    parsed = json.loads(result.text)
#    print(json.dumps(parsed['data']['children'][0], indent=2))
    for post in parsed['data']['children']:
            if any(keyword in post['data']['title'] for keyword in keywords):
                print(post['data']['title'])