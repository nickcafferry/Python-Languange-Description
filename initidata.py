#!/usr/bin/env python
# coding: utf-8

# Example 1-1. PP4E\Preview\initdata.py

# initialize data to be stored in files, pickles, shelves

#records
bob = {'name':'Bob Smith','age':42,'pay':30000,'job':'dev'}
sue = {'name':'Sue Jones','age':45,'pay':40000,'job':'hdw'}
tom = {'name':'Tom Caffrrey','age':50,'pay':50000,'job':None}

#database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key,'=>\n',db[key])





