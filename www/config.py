#!/usr/bin/python

import config_default

class Dict(dict):

	def __init__(self,name=(),value=(),**kw):

		super(Dict,self).__init__(**kw)

		for k,v in zip(name,value):

			self[k]=v

	def __getattr__(self,key):

		try:

			return self[key]

		except KeyError:

			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)


	def __setattr__(self,key,value):

		self[key]=value


def merge(defaults,override):

	r={}

	for k,v in defaults.items():

		if k in override:

			if isinstance(v,dict):

				r[k]=merge(v,override[k])

			else:

				r[k]=override[k]

		else:

			r[k]=v

	return r


def toDict(d):

	D=Dict()

	for x,y in d.items():

		D[x]=toDict(y) if isinstance(y,dict) else y

	return D





defaults=config_default.configs


try:

	import config_override

	configs=merge(defaults,config_override.configs)

except ImportError:

	pass


#we can use it as configs.db.host or we just can do like configs['db']['host']
configs=toDict(configs)

# print(configs.db.host)
# print(configs['db']['host'])

return configs