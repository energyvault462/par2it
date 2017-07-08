
#!/usr/bin/python
import os
import sys
import signal
import subprocess
from myqueue import Queue

# 2017 Brent Johnson
# https://github.com/energyvault462/par2it

class ParWrapper:
    def __init__(self):
        self.q = Queue()

    def TraverseFolder(self, baseFolder = "."):
        for root, dirs, files in os.walk(baseFolder):
            path = root.split(os.sep)
            for file in files:
                filestr = root
                filestr += "/"
                filestr += file
                self.q.enqueue(filestr)
            #self.q.printqueue()
            #print "- " *10
            #self.q.printqueue()
            self.CallPar(root)
            #print "-" * 10
            #self.q.printqueue()

    def CallPar(self, folder):
        targetfiles = ""
        folder.replace(" ", "\ ")
        if self.q.size() > 0:
            while (self.q.size() > 0):
                #print self.q.dequeue()
                targetfiles += "\"" + self.q.dequeue() + "\" "
            targetfiles.replace(" ", "-")
            parcommand = "par2 create "
            parcommand += "\"" + folder + "/par2it.par\" " + targetfiles
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