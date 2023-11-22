import argparse

parser = argparse.ArgumentParser(description="default")
parser.add_argument('data', type=str, help="initial data to encrypt")
parser.add_argument('key', type=int, help="key to encrypt the data")

args = parser.parse_args()

print("initial data : ", args.data)
print("key : ", args.key)
