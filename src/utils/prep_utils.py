from pathlib import Path


def get_tokens():
  secrets = open('./tokens.txt', 'r').read().splitlines()
  tokens = {}
  for secret in secrets:
    name, token = secret.split('=')
    tokens[name] = token
  return tokens


def prepare_logs_dir(dir='./logs'):
  if not Path(dir).exists():
    Path(dir).mkdir(parents=True, exist_ok=True)
    for ii in range(7):
      Path(dir + f'/{ii}.txt').touch()
    Path(dir + '/repeated_tries_count.txt').touch()
    f = open(dir + '/repeated_tries_count.txt', 'w', encoding='utf-8')
    f.write('0')
    f.close()
