#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     getFansNum.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-08 22:17:55
# MODIFIED: 2015-12-08 22:18:03

import sys
import os

if __name__ == '__main__':
    if(len(sys.argv) < 3):
        print "sys.argv[1]: input file!"
        print "sys.argv[2]: output file!"
        exit()
    
    user = {}
    with open(sys.argv[1], "r") as fin:
        for num, line in enumerate(fin):
            if num == 0:
                continue;
            if num % 100000 == 0:
                #break;
                print num
            userId, fansId = line.strip().split(",")
            #print userId
            #print fansId
            #exit()
            if userId not in user:
                user[userId] = 0
            else:
                user[userId] += 1

    #print user
    print "user done!"
    result = open(sys.argv[2], "w+")
    for key in user:
        result.write(str(key) + "\t" + str(user[key]) + "\n")
    result.close()
    print "write done!"
        
        
        
        
        