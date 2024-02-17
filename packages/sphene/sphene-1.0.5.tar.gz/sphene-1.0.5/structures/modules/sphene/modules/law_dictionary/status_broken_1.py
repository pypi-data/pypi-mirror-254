
'''
	python3 status.proc.py "modules/law_dictionary/status_broken_1.py"
'''

import sphene.modules.law_dictionary as law_dictionary

def broken_1 ():
	def problem (prob):
		return prob

	dictionary = {}
	the_problem = law_dictionary.check (	
		laws = {
			"directory": {
				"required": True,
				"contingency": "/",
				"allow": [ "/" ]
			}
		},
		dictionary = dictionary,
		
		problem = problem
	)
	
	print ("the problem:", the_problem)
	
	assert (
		the_problem == 
		'The label "directory" was not found in the laws.'
	)
	

def broken_2 ():
	def problem (prob):
		return prob

	dictionary = {
		"directory": "/",
		"directory 2": "/"
	}
	
	the_problem = law_dictionary.check (	
		laws = {
			"directory": {
				"required": True,				
				"allow": [ "" ]
			},
			"directory 2": {
				"required": True,
				"allow": [ "/" ]
			}
		},
		dictionary = dictionary,
		
		problem = problem
	)
	
	print ("the problem:", the_problem)
	
	assert (
		the_problem == 
		'Defintion "/" is not allowed.'
	)
	

checks = {
	'broken 1': broken_1,
	'broken 2': broken_2
}

