#!/usr/bin/python

def abc(**kw):

	print(kw)

	# for x,y in kw.items():

	# 	print(x,y)


	# for x,y in kw.items():
	for x,y in zip(kw):

		print(x,y)

dict1={'a':1,'b':2,'c':3}

dict2={'d':4,'e':5,'f':6}

l1=[1,2,3]
l2=[4,5,6]

# abc(a=1,b=2,c='ac')
abc(dict1=dict1,dict2=dict2)

# d=zip(dict2,dict1)
# d=zip(l1,l2)

# for x,y in d:

# 	print(x,y)
# print(d)