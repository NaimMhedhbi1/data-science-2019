# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:19:26 2019

@author: user
"""
/*
##
# Python's program to display all dates between two dates.
 
import datetime
 
start = datetime.datetime.strptime("2016-06-15", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-06-30", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
 
for date_object in date_array:
    print(date_object.strftime("%Y-%m-%d"))
    Sample output of above program.
C:\programs\time>pep8 --first example10.py

C:\programs\time>python example10.py
2016-06-15
2016-06-16
2016-06-17
2016-06-18
2016-06-19
2016-06-20
2016-06-21
2016-06-22
2016-06-23
2016-06-24
2016-06-25
2016-06-26
2016-06-27
2016-06-28
2016-06-29

C:\programs\time>

------------------------------------------------------
*/