## 2. Authenticating with the API ##

page = "https://oauth.reddit.com/r/python/top"
header = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get(page, headers = header, params = params)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top['data']
python_children = python_top_articles['children']
for i in python_children:
    if (i['data']['ups']) == 53:
        most_upvoted = i['data']['id']


## 4. Getting Post Comments ##

page = "https://oauth.reddit.com/r/python/comments/4b7w9u"

response = requests.get(page, headers = headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]['data']['children']

ups = 0
for i in comments_list:
    if (i['data']['ups']) > ups:
        ups = (i['data']['ups'])
        most_upvoted_comment = (i['data']['id'])


## 6. Upvoting a Comment ##

page = "https://oauth.reddit.com/api/vote"
payload = {"dir": 1, "id": "d16y4ry"}
response = requests.post(page, json=payload, headers=headers)
status = response.status_code