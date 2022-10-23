#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:03:02 2022

@author: pengxiao
"""

#python program to illustrate the concept
#of the threading
#importing the threading module
import threading
import os

def task1():
    print('task1 assigned to thread: {}'.format(threading.current_thread().name))
    print('ID of process running task 1: {}'.format(os.getpid()))
    
def task2():
    print('task2 assgined to thread: {}'.format(threading.current_thread().name))
    print('ID of process running task 2: {}'.format(os.getpid()))
    
    
if __name__=='__main__':
    
    #print current process
    print('ID of process running main program: {}'.format(os.getpid()))
    
    #print main thread name
    print('Main thread name: {}'.format(threading.current_thread().name))
    
    
    #creating threads
    t1=threading.Thread(target=task1, name='t1')
    t2=threading.Thread(target=task2, name='t2')
    
    #start threads
    t1.start()
    t2.start()
    
    #wait until all the threads are finished
    t1.join()
    t2.join()
    
    print('Main thread name: {}'.format(threading.current_thread().name))