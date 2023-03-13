__version__ = '1.0'
__author__ = 'Andreas Paraskeva'

from pyexpat import model
import pandas as pd

# Local imports 
from src.utils import get_parser

def main():
  parser = get_parser()
  args = parser.parse_args()

  if args.mode == 'preprocess':
    # TODO: Add preprocessing code here
    exit('Preprocessing code not implemented yet!')
  elif args.mode == 'train':
    # TODO: Add training code here
    exit('Training code not implemented yet!')
  elif args.mode == 'inference':
    # TODO: Add inference code here
    exit('Inference code not implemented yet!')
  else:
    exit('Invalid option type provided!')


if __name__ == '__main__':
  main()