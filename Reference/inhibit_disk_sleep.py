# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 13:13:32 2014

@author: canton
"""
import time, random

filename = "inhibit-sleep.txt"
counter = 0
mymax   = 1000


def writeFile(filename, content):
    'write a file'
    with open(filename, 'a') as f:
        f.write(str(content)+"\n")


if __name__ == "__main__":
    while counter < mymax:
        rnd = random.randint(10000, 19999)
        #print(rnd)
        writeFile(filename, rnd)
        counter += 1
        time.sleep(1)