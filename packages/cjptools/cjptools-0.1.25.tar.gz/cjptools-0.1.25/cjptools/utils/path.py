import os
import sys
import re


def getProjRoot():
    thePath = os.getcwd()
    while True:
        if os.path.exists(thePath + '/.idea'):
            sys.path.append(thePath)
        if thePath == '/' or thePath == '\\':
            break;
        thePath = os.path.dirname(thePath)


def getExpName(pyFileName):
    ss = pyFileName.split(".")
    expName = ss[0];
    pattern = r'^\d+$'
    if re.match(pattern, ss[1]):
        subExpId = int(ss[1])
    else:
        subExpId = 0;
    return (expName, subExpId)
