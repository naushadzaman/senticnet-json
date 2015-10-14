#!/usr/bin/python

import os 
import re 
import sys 
import time
import json 

filepath = os.path.abspath(os.path.dirname(__file__))

senticnet3_json = filepath+'/senticnet3_json.txt'

def load_senticnet3_json(senticnet3_json): 
	_dict = {} 
	for line in open(senticnet3_json): 
		line = line.strip()
		if line == '': 
			continue
		line = json.loads(line)
		_dict[line['word']] = line 
	return _dict


_dict = load_senticnet3_json(senticnet3_json)

if __name__ == '__main__':	
	word = 'written communication'
	sentic_output = _dict[word]
	print(sentic_output)
	