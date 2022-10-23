# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import threading


def thread_job():
    print('This is an added Thread,number is %s'%threading.current_thread())
    

def main():
    added_thread=threading.Thread(target=thread_job) #这里是定义好了thread
    added_thread.start()                             #真正地去执行它
'''
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())  #当我在运行该程序的时候，运行的线程
'''
if __name__=='__main__':
    main()