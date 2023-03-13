import argparse

def get_parser():
  '''
  Method to create arguement parser

  Output:
    - parser: the arguement parser
  '''
  parser = argparse.ArgumentParser()
  parser.add_argument(
                        '--verbose', 
                        action=argparse.BooleanOptionalAction, 
                        default=False,
                        help='Choose verbose mode: \n \
                          \t- no-verbose: no prints\
                          \t- verbose: prints enabled'
                      )
  parser.add_argument(
                        '--mode', 
                        choices=['preprocess', 'train', 'inference'], 
                        default='train', 
                        required=False, 
                        help='Choose type of mode used: \n \
                          \t- preprocess: initialize data preprocessing\n\
                          \t- train: train the chosen model\n\
                          \t- eval: evaluate the chosen model'
                    )
  parser.add_argument(
                        '--device', 
                        choices=['cpu', 'cuda', 'mps'], 
                        default='cpu', 
                        required=False, 
                        help='Choose device to be used: \n \
                          \t- cpu: train/inference on cpu\
                          \t- cuda: train/inference on gpu\
                          \t- mps: train/inference on apple silicon gpu'
                    )

  return parser