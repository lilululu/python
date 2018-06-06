#!/usr/bin/python

import inspect

def a(a,b=0,*c,d,e=1,**f):

	pass

aa=inspect.signature(a)

print(aa)

print(type(aa))

