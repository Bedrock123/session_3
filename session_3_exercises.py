"""
Zachary Bedrosian
Session 3 Exercises
9.10.2017
"""

"""
1. Below is a transcript of a session with the Python shell. For each expression being evaluated, 
provide the type and the value the expression returns.I encourage you to answer them directly
since this will help reinforce your understanding of basic Python expressions.
"""
import time
import datetime

# 1.1
a = 3
a + 2
print(a)

# 1.2
a = a + 1.0
a
# converts into a float
print(a)

# 1.3
a = 3
# b runs an arror becuase b is not defined

# 1.4
a = 3
print(a == 5.0) # a does not equal 5.0
a 
print(a) 

# 1.5
b = 10
c = b > 9
c 
print(c) # 10 is great then 10, the variable c holds the boolean value True

# 1.6
print(5/2 == 5/2.0) # Dividing by a float will yeild a different decmical place number

"""
2. For each of the following expressions, indicate the value returned. I encourage you to answer them 
directly since this will help reinforce your understanding of basic Python expressions.
"""

# 2.1
# 3 minus 1 does not equal 5 minus 3
print(3.0 - 1.0 != 5.0 - 3.0) # False 2 does 2

# 2.2
# 3 is not greater then 4. 2 is less then 3, but 9 is not greater then 10 so it is False.
print(3 > 4 or (2 < 3 and 9 > 10))

# 2.3
# 4 is not greater 3, but 3 is less then 4 and 9 is greater 8 so it evalutates to True
print(4 > 5 or 3 < 4 and 9 > 8)

# 2.4
# 4 is greater then 3, and 100 is greater 6 then so it evaluates as True
# But then not turns it to False
print(not(4 > 3 and 100 > 6))

"""
3. The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”,
which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.
"""

current_epoch_time = time.time()
unix_epoch = datetime.datetime(1971,1,1,0,0)
current_date = datetime.datetime.now()
difference = current_date - unix_epoch
human_format_time = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(current_epoch_time))

print(difference.days, " Days Since Epoch")
print("Current Date: " + human_format_time)