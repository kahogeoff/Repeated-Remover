__author__ = 'Geoffrey Cheung'
# coding: utf-8
from os import listdir, remove
from os.path import isfile, join, split
from hashlib import md5, sha1
from fileobj import fileObject

fileList = []
sortedList = []
debug = False
path = ''
debug_path = "C:\Users\Geoffrey&Gillian\Desktop\Test Folder"


def isSameFile(pth1, pth2):
    pth1_md5 = md5(open(pth1).read()).hexdigest()
    pth2_md5 = md5(open(pth2).read()).hexdigest()
    if pth2_md5 == pth1_md5:
        return True
    else:
        return False


if debug:
    path = debug_path


def GetList(pth):
    for f in listdir(pth):
        if isfile(join(pth, f)):
            tmp_pth = join(pth, f)
            fileList.append(fileObject(tmp_pth, md5(open(tmp_pth).read()).hexdigest()))


def GetRepeated():
    while len(fileList) > 0:
        cur_item = fileList.pop(0)
        for item in fileList[:]:
            if cur_item.getHashCode() == item.getHashCode():
                cur_item.addRepeatedItem(item)
                fileList.remove(item)
        sortedList.append(cur_item)


def RemoveRepeated():
    for fileItem in sortedList:
        if fileItem.getRepeatedItems():
            for i in fileItem.getRepeatedItems()[:]:
                remove(i.getFilePath())
                fileItem.getRepeatedItems().remove(i)
