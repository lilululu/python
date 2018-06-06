#!/usr/bin/python

import inspect

def a(a,b=0,*c,d,e=1,**f):

	pass

aa=inspect.signature(a)

parameters=aa.parameters

args=[]

for name,param in parameters.items():

	

	if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)

print(args)
# print(aa.parameters)

# print(type(aa))

