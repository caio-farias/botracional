import actions

token = open('tokens.txt','r').read().splitlines()

API_KEY             = token[0]
API_SECRET_KEY      = token[1]
ACCESS_TOKEN        = token[2]
ACCESS_TOKEN_SECRET = token[3]

api = actions.auth(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
t = api.home_timeline(count=1, exclude_replies=True)
tweet_count = t[0].__dict__["user"].statuses_count
actions.start_bot(api, tweet_count)