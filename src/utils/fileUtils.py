import os

def getRootDir():
    return os.getcwd()

def getDatasetFile():
    return getRootDir() + '/dataset/basedata/all-data.dat'

def getDatasetDir():
    return getRootDir() + '/dataset/parsingdata'

def getAllLineFromDataset(path=''):
    file = open(getDatasetDir() + '/' + path, 'r')
    lines = file.readlines()
    file.close()
    return lines