from fabric.api import *

'''
OPS435 Assignment 2S - Fall 2020
Program: a2r_mkobzar.py
Author: Maxim Kobzar
The python code in this file a2s_mkobzar.py is original work written by
Maxim Kobzar. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''

# set the name of the user login to the remote host
env.user = 'student'
env.port = '7517'
env.hosts = ['myvmlab.senecacollege.ca']
env.password = '0dc7Rnr*%E'

def addUser(name):
    '''add a user with given user name to remote system'''
    
    cmd1 = 'adduser ' + name + ' -m'
    sudo(cmd1)

def listUser():
    '''return a list of shell user on a remote system'''
    

    #save remote file output to list, split by \n.
    file = run('cat /etc/passwd')
    file = file.split('\n')

    #test for shell users in list
    shell_user = []
    for item in file:
        if item.count("/bin/bash") != 0:
            shell_user.append(item)
  
    #parse user info.
    parsed_user = []
    for item in shell_user:
        parsed_user.append(item.split(":"))
    
    #create list of names of correct users
    name_user = []
    for user in parsed_user:
        name_user.append(user[0])
    print(name_user)


def listSysUser():
    '''return a list of system (non-shell) user'''
    
    #save remote file output to list, split by \n.
    file = run('cat /etc/passwd')
    file = file.split('\n')
    
    #test for sys user in list.
    sys_user = []
    for item in file:
        if item.count("/sbin/nologin") != 0:
            sys_user.append(item)
        
    #parse user info
    parsed_user = []
    for item in sys_user:
        parsed_user.append(item.split(":"))
        
    #create list of correct users
    name_user = []
    for user in parsed_user:
        name_user.append(user[0])
    print(name_user)



def findUser(name):
    '''find user with a given user name'''

    #save remote file output to list, split by \n.
    file = run('cat /etc/passwd')
    file = file.split('\n')
        
    #parse user info.
    parsed_user = []
    for item in file:
        parsed_user.append(item.split(":"))
        
    #create list of all users.
    name_user = []
    for user in parsed_user:
        name_user.append(user[0])
    
    #test for the given user.
    try:
        name_user.index(name)
        print('Found user ' + name + ' on the system.')
    
    except ValueError:
        print('User ' + name + ' not on the system.')
           
    


    

