
import argparse
import sys
import os
from lib.node import Node

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

def parse_dataset(data):
    dataset = []
    for line in data:
        stripped = line.strip()
        split = stripped.split()
        row = [int(val) for val in split[:-1]] + [split[-1]]
        dataset.append(row)
    return dataset

if __name__ == "__main__":
    # args = parse_args()

    # if args.test:
    #     run_tests("lib/tests.py")

    filename = "data/monks-1.test"

    # data = open(args.filename, 'r')
    data = open(filename, 'r')

    dataset = parse_dataset(data)

    root_node = Node(dataset)

    root_node.build_tree()

    # print(root_node)

    

