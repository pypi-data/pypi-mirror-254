import time


def getTime():
    return time.perf_counter()


theTic = 0


def tic():
    global theTic
    theTic = time.perf_counter()
    return theTic


def toc(timeObj=None):
    if timeObj is not None:
        return time.perf_counter() - timeObj;
    else:
        return time.perf_counter() - theTic;
