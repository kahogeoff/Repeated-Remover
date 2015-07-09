__author__ = 'Geoffrey&Gillian'
import os

class fileObject:
    def __init__(self, path, hashcode):
        self.path = path
        self.hashcode = hashcode
        self.repeated = []

    def addRepeatedItem(self, item):
        self.repeated.append(item)

    def getRepeatedItems(self):
        return self.repeated

    def getHashCode(self):
        return self.hashcode

    def getFilePath(self):
        return self.path

    def getFileName(self):
        name = os.path.split(self.path)[1]
        return name