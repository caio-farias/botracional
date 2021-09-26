from src.actions import auth, user_info, start_bot
from src.utils.prep_utils import get_tokens, prepare_logs_dir

def main():
  prepare_logs_dir()

  tokens = get_tokens()

  API_KEY             = tokens['API_KEY']
  API_KEY_SECRET      = tokens['API_KEY_SECRET']
  ACCESS_TOKEN        = tokens['ACCESS_TOKEN']
  ACCESS_TOKEN_SECRET = tokens['ACCESS_TOKEN_SECRET']

  api = auth(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  t = api.home_timeline()
  user = api.get_user('botracional')
  user_info(user)
  try:
    tweet_count = t[0].__dict__["user"].statuses_count
  except:
    tweet_count = 0
  start_bot(api, tweet_count)

if __name__ == 'main.py':
  main()