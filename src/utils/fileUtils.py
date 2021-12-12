import os

def getRootDir():
    return os.getcwd()

def getDatasetFile():
    return getRootDir() + '/dataset/basedata/all-data.dat'

def getAllLineFromDataset():
    file = open(getDatasetFile(), 'r')
    lines = file.readlines()
    file.close()
    return lines
