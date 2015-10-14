Author: Naushad UzZaman (n@uzzaman.com) 

This is a json output version of SenticNet 3! 
The author was having issues with different SenticNet tools because of: 
* problem in loading RDF/XML format -- https://github.com/yurimalheiros/senticnetapi
* time takes to get the results from API -- https://github.com/tanayz/senticnetapi

Hence the author wrote scripts to create a json format output for SenticNet. Others having issues with existing tools could be benefited from it too. 

Note, the author of this tool is not affiliated with SenticNet authors. 
Please acknowledge the authors by citing the following publication
in any research work or presentation containing results obtained
in whole or in part through the use of SenticNet 3:

E. Cambria, D. Olsher, and D. Rajagopal. SenticNet 3: A Common and Common-Sense Knowledge Base for Cognition-Driven Sentiment Analysis. In: AAAI, pp. 1515-1521, Quebec City (2014)


# How to use the tool
If you don't want to re-generate the output, you can use the output: senticnet3_json.txt

# Usage : load SenticNet values for concepts/words 
```
$ python 
>>> import get_senticnet_values
>>> word = 'written communication'
>>> sentic_output = get_senticnet_values._dict[word]
>>> print(sentic_output)
{u'polarity': 0.095, u'word': u'written communication', u'sensitivity': 0.0, u'attention': 0.107, u'aptitude': 0.156, u'pleasantness': 0.021, u'semantics': [u'correspondence', u'note_down', u'document', u'handwritten', u'communication_method']}
```

# If you want to generate the output again
If you do not have necessary permissions, you can install it in a directory.
- install virtualenv
```
$ virtualenv venv
$ source venv/bin/activate
```

# Installations  
```
$ pip install -r requirements.txt
```

# Usage: Generating the json output 
I already provide tools to convert SenticNet rdf/xml format to json format. If you need to modify it, or change the input/output files in the script, feel free to do so in convert_sentic_rdf2json.py.
if you want to re-generate the file, run: 
```
$ python convert_sentic_rdf2json.py
```
