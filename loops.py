#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    
    n = 0
    
    if True: print 'True'
    
    for letra in 'lista':
        print letra
    
    for idx, item in enumerate('lista'):
        print idx, item
    
    for i in range(3):
        if i == 0:
            print i
        elif i == 1:
            print i
        else:
            print i
            
    while n < 4:
        print n
        n += 1
        