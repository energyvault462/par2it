
#!/usr/bin/python
import sys
from parwrapper import ParWrapper

# 2017 Brent Johnson
# https://github.com/energyvault462/par2it
# TODO: Travis CI tests

def main(argv):
    p = ParWrapper()
    if len(sys.argv) > 1:
        p.TraverseFolder(sys.argv[1])
    else:
        p.TraverseFolder()

if __name__ == "__main__":
    main(sys.argv)