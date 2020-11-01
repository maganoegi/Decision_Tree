
import argparse
import sys
import os
from lib import *

def run_tests(filename):
    GREEN = "\033[92m"
    END = "\033[0m"
    print(f"\nexecuting tests in {GREEN}{filename}{END}\n")
    fileDir = os.path.dirname(os.path.abspath(__file__))
    os.system(f"python3 {fileDir}/tests.py")

def parse_args():
    parser = argparse.ArgumentParser(description='Build a decision tree around the dataset')
    parser.add_argument('-t', '--test', default=False, action='store_true', help='run the tests instead of the main sequence')
    parser.add_argument("filename", help="name of the dataset file", type=str)
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()

    if args.test:
        run_tests("lib/tests.py")

    # dataset = open(args.filename, 'r')

    # root_node = 

