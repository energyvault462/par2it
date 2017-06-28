
#!/usr/bin/python
import os
#import fnmatch
import sys
import signal
from myqueue import Queue

class ParWrapper:
    def __init__(self):
        self.q = Queue()

    def TraverseFolder(self, baseFolder = "."):
        for root, dirs, files in os.walk(baseFolder):
            path = root.split(os.sep)
            for file in files:
                self.q.enqueue(self.FullPath(path, file))
            #self.q.printqueue()
            print "-" *10
            self.CallPar()
            print "-" * 10
            #self.q.printqueue()

    def CallPar(self):
        while (self.q.size() > 0):
            print self.q.dequeue()

    def FullPath(self, path, file):
        newpath = ""
        if not self.q.isEmpty():
            for item in path:
                newpath += item
                newpath += "/"
            newpath += file
            #print(newpath)
            return newpath

def main(argv):
    p = ParWrapper()
    if len(sys.argv) > 1:
        p.TraverseFolder(sys.argv[1])
    else:
        p.TraverseFolder()

if __name__ == "__main__":
    main(sys.argv)