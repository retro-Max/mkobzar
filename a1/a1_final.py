#!/usr/bin/env python3
''' Converts a YYYMMDD, YYYY/MM/DD, YYYY-MM-DD, YYYY.MM.DD date format into a Month name-Day-Year date format.

This program will take a command line argumnet as a date in the format outlined in usage() and
return the date argument in a standard format: 'mmm d, yyyy", where "mmm" is the three letter
abbreviated month's name, 'd' is a one or two-digit day of the month, and 'yyyy' is the four
digit year.

-----------------------------------------------------------------------
OPS435 Assignment 1 - Fall 2020
Program: a1_mkobzar.py
Author: Maxim Kobzar
The python code in this file (a1_mkobzar.py) is original work written by
"Maxim Kobzar". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

References
----------
https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
'''



import os
import sys


def leap_year(func_year):
    '''
    Determines leap year using the an algorithm from. 
    Returns a boolean.
    '''

    # 1)If the year is evenly divisible by 4, go to step 2. Otherwise, NOT leap year.
    if (func_year % 4) == 0:
        # 2)If the year is evenly divisible by 100, go to step 3. Otherwise, IS leap year.
        if (func_year % 100) == 0:
            # 3)If the year is evenly divisible by 400, then IS leap year. Otherwise, NOT leap year.
            if (func_year % 400) == 0:
                leap_flag = True
            else:
                leap_flag = False
        else:
            leap_flag = True
    else:
        leap_flag = False

    return leap_flag


def sanitize(user_input, test_chars):
    '''
    Removes any characters what are not in the allowed
    characters variable then returns the results.
    '''

    for char in user_input:
        if char not in test_chars:
            user_input = user_input.replace(char, '')

    return user_input


def size_check(user_input, size):
    '''
    Takes the user input and a integer size digit as arguments and checks
    if the length of the user input is equal to the specified size. IF the
    size is equal then True, False if not equal.
    Returns a boolean.
    '''

    if len(user_input) == int(size):
        status = True
    else:
        status = False

    return status


def range_check(value, range_size):
    '''
    Takes the sanitized user input as an int value and a range_size tuple as arguments
    then compares the value to the range_size and returns a False status if outside of range_size,
    True if within the range_size.
    Returns a boolean.
    '''
    if value < range_size[0]:
        status = False

    elif value > range_size[1]:
        status = False
    else:
        status = True

    return status


def usage():
    '''
    This function takes no argument and outputs to the standard output, the expected
    format of the command line argument.
    '''
    return "Usage: a1_mkobzar.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"



if __name__ == "__main__":
    # step 1
    if len(sys.argv) != 2:
        print(usage())
        sys.exit()
        
    # step 2
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    user_raw_data = sys.argv[1]
    
    # step 3
    allow_chars = '0123456789'
    dob = sanitize(user_raw_data, allow_chars)
    # removed print('Sanitized user data:', dob) to pass check.py, template differs from check script.
    
    # step 4
    result = size_check(dob, 8)
    if result == False:
        print("Error 09: wrong date entered")
        sys.exit()
        
    # step 5
    year = int(dob[0:4])
    month = int(dob[4:6])
    day = int(dob[6:])
    
    # step 6
    result = range_check(year, (1900, 9999))
    if result == False:
        print("Error 10: year out of range, must be 1900 or later")
        sys.exit()
    result = range_check(month, (1, 12))
    if result == False:
        print("Error 02: wrong month entered")
        sys.exit()
    result = leap_year(year)
    if result == True:
        days_in_month[2] = 29
    result = range_check(day, (1, days_in_month[month]))
    if result == False:
        print("Error 03: wrong day entered")
        sys.exit()
        
    # step 7
    new_dob = str(month_name[month - 1]) + ' ' + str(day) + ', ' + str(year)
    
    # step 8
    # removed print("Your date of birth is:", new_dob) in order to pass checkA1.py script.
    print(new_dob)

