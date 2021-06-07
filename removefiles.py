import time
import os
import shutil

path = 'C:/Users/ratho/Downloads'
days = 60
seconds = time.time() - (days *24*60*60)

if os.path.exists(path): 
    print("PATH EXIsTS")

for rootfolder, folders, files in os.walk(path):
    for folder in folders:
        folderpath = os.path.join(rootfolder,folder)
    
ctime = os.stat(path).st_ctime 

if seconds >= ctime:
    os.remove(path)
    shutil.rmtree()


    