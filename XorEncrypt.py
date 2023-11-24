import argparse

parser=argparse.ArgumentParser(description="default")
parser.add_argument('given',type=str,help="This is the data to be encoded")
parser.add_argument('key',type=int,help="This is the key to encrypt the given data")
args=parser.parse_args()
given=args.given
key=args.key

print("crypto{",end="")
for x in given:
	print(chr(ord(x)^key),end="")
print("}")
