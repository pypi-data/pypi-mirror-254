
'''
	import story_1.treasury.climate as treasury_climate
	offline_climate = treasury_climate.retrieve ()
'''

import os
from os.path import dirname, join, normpath
import pathlib
import sys

climate = {
	"elected safe": {},
	"paths": {}
}

def build (
	CWD = None
):
	#offline_goods = str (normpath (join (CWD, "offline_goods")))
	treasury = str (normpath (join (CWD, "treasury")))

	#if (os.path.isdir (offline_goods) != True):
	#	os.mkdir (offline_goods)
		
	if (os.path.isdir (treasury) != True):
		os.mkdir (treasury)

	#climate ["paths"] ["offline_good"] = offline_goods
	climate ["paths"] ["treasury"] = treasury
	

	return;


def retrieve ():
	return climate