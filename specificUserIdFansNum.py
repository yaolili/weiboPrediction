#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     specificUserIdFansNum.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-08 22:55:50
# MODIFIED: 2015-12-08 22:55:52

import sys
import os

if __name__ == '__main__':
    if(len(sys.argv) < 4):
        print "sys.argv[1]: fansNum.txt!"
        print "sys.argv[2]: all_user_uniq.txt!"
        print "sys.argv[3]: output file!"
        exit()
    
    result = open(sys.argv[3], "w+")
    specificUser = {}
    with open(sys.argv[2], "r") as fin:
        for userId in fin:
            id = userId.strip().split("\n")
            specificUser[id[0]] = 0
    
    print "specificUser done!"
    #print specificUser
    with open(sys.argv[1], "r") as fin:
        for line in fin:
            userId, fansNum = line.strip().split("\t")
            if userId in specificUser:
                result.write(str(userId) + "\t" + str(fansNum) + "\n")
    
    print "write done!"
    result.close()
            