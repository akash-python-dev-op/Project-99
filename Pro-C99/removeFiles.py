import os
import shutil
import time

path = 'D:\Others\Pro-C99\removeFiles.py'
seconds = 864000

desiredTime = time.time(days)
os.path.exists.path(path)
os.walk(path)
os.path.join(removeFiles.py,path)
ctime = os.stat(path).st_ctime

if ctime>desiredTime:
    os.remove(path)
