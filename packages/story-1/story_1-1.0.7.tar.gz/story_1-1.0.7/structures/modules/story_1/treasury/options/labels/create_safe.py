
'''
	
'''

'''
	create_treasury
	
	fields {
		"label": ""
	}
'''

'''
	(mo)net
	monay
	monayuh
	monaym
'''

import story_1.treasury.climate as treasury_climate

import os
from os.path import dirname, join, normpath
import pathlib
import sys

def play (JSON):
	print ('create safe', JSON)
	offline_climate = treasury_climate.retrieve ()

	treasurys_paths = offline_climate ["paths"] ["treasury"]
	fields = JSON ["fields"]
	
	if ("label" not in fields):
		return {
			"obstacle": f'Please choose a "label" for the safe.'
		}
	
	treasury_label = fields ["label"]
	treasury_path = str (normpath (join (treasurys_paths, treasury_label)))

	if (os.path.isdir (treasury_path) != True):
		os.mkdir (treasury_path)
		treasury_climate.climate ["elected safe"] ["path"] = treasury_path
		return {
			"victory": "safe created"
		}
		
	else:
		treasury_climate.climate ["elected safe"] ["path"] = treasury_path
		return {
			"obstacle": "There is already a directory at that path"
		}
