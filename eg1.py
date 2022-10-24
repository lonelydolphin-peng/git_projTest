#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:21:24 2022

@author: pengxiao
"""

#python program to illustrate the concept
#of the threading
#importing the threading module
import threading

def print_cube(num):
    print('cube: {}\n'.format(num*num*num))
    
def print_square(num):
    print('square: {}\n'.format(num*num))
    
if __name__=='__main__':
    #creating thread
    t1=threading.Thread(target=print_square, args=(10,))
    t2=threading.Thread(target=print_cube, args=(10,))
    
    #starting thread 1
    t1.start()
    #starting thread 2
    t2.start()
    
    #wait until thread 1 is completely executed
    t1.join()
    #wait until thread 2 is completely excuted
    t2.join()
    
    #both thread is completely excuted
    print('all done!')
    print("duanshipin")
    print("yuefan")
    
