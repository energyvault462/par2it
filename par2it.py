
#!/usr/bin/python
import os
import sys
import signal
import subprocess


# 2017 Brent Johnson
# https://github.com/energyvault462/par2it

class ParWrapper:

    def TraverseFolder(self, baseFolder = "."):
        for root, dirs, files in os.walk(baseFolder):
            self.CallPar(root)


    def CallPar(self, path):
        parcommand = "par2 create "
        parcommand += "\"" + path + "/.par2it\" \"" + path + "/*\""
        print "-" * 10
        print "callpar: %s" % parcommand
        subprocess.call(parcommand, shell=True)
        print "-" * 10

def main(argv):
    p = ParWrapper()
    if len(sys.argv) > 1:
        p.TraverseFolder(sys.argv[1])
    else:
        p.TraverseFolder()

if __name__ == "__main__":
    main(sys.argv)