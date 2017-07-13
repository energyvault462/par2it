import os
import signal
import subprocess

class ParWrapper:
    def TraverseFolder(self, baseFolder = "."):
        for root, dirs, files in os.walk(baseFolder):
            if self.VerifyPars(root) > 0:
                self.CreatePars(root)

    def GetParList(self, path):
        import glob
        searchstr = path + "/.par2it*"
        list = glob.glob(searchstr)
        return list

    def VerifyPars(self, path):
        filesToCheck = ""
        exitcode = 0
        parfiles = []
        parfiles = self.GetParList(path)
        if len(parfiles) == 9:
            for parfile in parfiles:
                filesToCheck += "\"" + parfile + "\" "
            parcommand = "par2 v "
            parcommand += filesToCheck
            rc = subprocess.call(parcommand, shell=True)
            if rc > 0:
                exitcode = rc
        else:
            exitcode = 999
        return exitcode

    def DeleteParFiles(self, path):
        parfiles = self.GetParList(path)
        for parfile in parfiles:
            try:
                os.remove(parfile.encode('unicode_escape'))
            except OSError:
                pass

    def CreatePars(self, path):
        self.DeleteParFiles(path)
        parcommand = "par2 create -n8 "
        parcommand += "\"" + path + "/.par2it\" \"" + path + "/*\""
        subprocess.call(parcommand, shell=True)