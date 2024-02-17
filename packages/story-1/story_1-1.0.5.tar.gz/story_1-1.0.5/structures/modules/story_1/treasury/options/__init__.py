

'''
	{
		"label": "",
		"fields": {
			
		}
	}
'''

import json
from os.path import dirname, join, normpath
import os

import story_1.treasury.options.labels.create_safe as create_safe
import story_1.treasury.options.labels.form_proposal_keys as form_proposal_keys

def records (record):
	print (record)

def play (
	JSON = "",
	records = records
):
	print ("JSON:", JSON)

	if ("label" not in JSON ):
		records (f'Options need a "label".')
		return;

	label = JSON ["label"]
	
	print ("label:", label)
	
	if (label == "create safe"):
		return create_safe.play (JSON)
	elif (label == "form proposal keys"):
		return form_proposal_keys.play (JSON)

	return {
		"obstacle": f'An option with label "{ label }" was not found.'
	}
