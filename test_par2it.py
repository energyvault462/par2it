import pytest
import os, io

from parwrapper import ParWrapper

def createtestfiles():
    filelist = [".par2it.par2", ".par2it.vol000+01.par2", ".par2it.vol001+02.par2", ".par2it.vol003+04.par2", ".par2it.vol007+08.par2"]
    for file in filelist:
        with io.open("./tests/" + file, 'w', encoding='utf-8') as f:
            f.write(u'test')

@pytest.yield_fixture()
def parwrapper():
    createtestfiles()
    pw = ParWrapper()
    yield pw
    pw.DeleteParFiles('./tests')

def test_getparlist(parwrapper):
    parlist = parwrapper.GetParList('./tests')
    assert len(parlist) == 5