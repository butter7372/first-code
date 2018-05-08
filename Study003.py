#更改文件名或者扩展名的案例
import time
import os
import random
print(os.curdir)
os.chdir(".\pystudy")
files=os.listdir(".")
print(files)
for file in files:
    ext =  os.path.splitext(file)
    if ext[1] == ".txt":
        print(ext[0])
        A = ext[0]
        print(A)
        B = "Test" + str(random.randint(1, 100))
        print(B)
        newext = B + ".csv"
        os.rename(file, newext)