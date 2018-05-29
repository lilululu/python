#!/usr/bin/python

import orm

from model import Users

import asyncio

@asyncio.coroutine

def test():

	yield from orm.create_pool(loop=loop,user='root',password='walMl12%',db='awesome')

	# u=Users(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
	u=Users(name='dflhuang', email='dflhuang@qq.com', passwd='0123', image='about:blank',id='110')

	yield from u.save()


loop=asyncio.get_event_loop()

loop.run_until_complete(test())

loop.close()

# for x in test():

# 	print(x)