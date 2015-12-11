#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     getUserType.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-10 21:20:16
# MODIFIED: 2015-12-10 21:25:46

import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "sys.argv[1]: unique user file!"
        print "sys.argv[2]: weibo user!"
        print "sys.argv[3]: output file!"
	exit()

    allUser = {}
    result = file(sys.argv[3], "w+")
    with open(sys.argv[1], "r") as fin:
        for line in fin:
            aList = line.strip().split("\n")
            if aList:
                userId = aList[0]
                allUser[userId] = 0
                #allUser.append(userId)
            else:
                print "unique user file split error!"
                exit()

    print "allUser done!"
    #print allUser
    #exit()

    with open(sys.argv[2], "r") as fin:
        for num, line in enumerate(fin):
            if num == 0:
                continue
            if num % 10000 == 0:
                print num
            aList = line.strip().split(",")
            if(aList):
                '''
                print aList
                print len(aList)
                print type(aList[0])
                print aList[4]
                exit()
                '''
                if len(aList) >= 5:
                    if aList[4] in allUser:
                        print "match!"
                        if aList[0] == 'false':
                            flag = 0
                        elif aList[0] == 'true':
                            flag = 1
                        else:
                            flag = -1                   
                        result.write(aList[4] + "\t" + str(flag) + "\n")    
                    #else:
                        #print num
                        #print aList[4]
                        #print type(aList[4])
                        #exit()
                else:
                    #print "line num: "
                    #print num
                    continue
            else:
                print "split error!"
                exit()
                
    result.close()