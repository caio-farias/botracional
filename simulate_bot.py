from src.simulation_actions import start
from src.utils.prep_utils import prepare_logs_dir

def main():
  prepare_logs_dir()
  start()


if __name__ == 'main.py':
  main()