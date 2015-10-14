#!/usr/bin/python

import os 
import re 
import sys 
import time
import json 
from bs4 import BeautifulSoup

filepath = os.path.abspath(os.path.dirname(__file__))

def load_senticnet(): 
	rdf_text = open(filepath+'/senticnet3.rdf.xml').read() 
	_text = re.sub(r'[\n\r]', ' ', rdf_text) 
	_text = re.sub('<rdf:Description rdf:about', '\n<rdf:Description rdf:about', _text)
	_text = re.sub('</rdf:Description>', '</rdf:Description>\n', _text)

	_text_split = _text.split('\n')
	return _text_split
	

def create_json_senticnet(): 
	_text_split = 	load_senticnet() 
	outfile = open(filepath+'/senticnet3_json.txt', 'w')
	for each in _text_split: 
		each = re.sub('>', '>\n', each)
		soup = BeautifulSoup(each)
		semantics = []
		_dict = {}
		try: 
			_dict['word'] = soup.findAll('text')[0].get_text().strip() 
			for affect in ['pleasantness', 'attention', 'sensitivity', 'aptitude', 'polarity']: 
				text = soup.findAll(affect)[0].get_text().strip() 
				_dict[affect] = float(text)
		except: pass 
		for entry in soup.findAll('semantics'):
			entry_attrs = dict(entry.attrs)
			semantics.append(re.sub('http://sentic.net/api/en/concept/', '', entry_attrs['rdf:resource']))
		
		_dict['semantics'] = semantics
		if not 'word' in _dict: continue
		outfile.write(json.dumps(_dict) + '\n\n')
	
	outfile.close()		


if __name__ == '__main__':	
	create_json_senticnet() 
	