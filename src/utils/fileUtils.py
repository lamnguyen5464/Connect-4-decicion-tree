import os

def getRootDir():
    return os.getcwd()

def getDatasetDir():
    return getRootDir() + '/dataset'

def getAllLineFromDataset(path=''):
    file = open(getDatasetDir() + '/' + path, 'r')
    lines = file.readlines()
    file.close()
    return lines