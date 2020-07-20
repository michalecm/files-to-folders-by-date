import sys
import os
import subprocess
import urllib.parse as urlparse
import shutil
from datetime import datetime as dt
import platform
import errno

#accept command line input with sys module - file path

def main():
    path = sys.argv[1]
    fileList = []
    tmpList = os.listdir(path)
    for f in tmpList:
        if os.path.isfile(os.path.join(path, f)):
            fileList.append(os.path.join(path, f))

    for fileName in fileList:
        if os.access(fileName, os.W_OK):
            edate = (dt.fromtimestamp(creationDate(fileName))).strftime('%Y-%m-%d')
            newfold = path + str(edate)
            try:
                os.mkdir(newfold)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            shutil.move(fileName, newfold)

def creationDate(path_to_file):
    print(os.stat(path_to_file).st_mtime)
    return os.stat(path_to_file).st_mtime
                                
if __name__=="__main__":
    main()