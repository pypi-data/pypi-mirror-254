
'''
	{
		dictionary_health,
		dictionary_trends,
		law_dictionary,
		dictionary_customs,
		dictator,
		tater,
		potatoe,
		potato salad,
		vegan_butter
	}
'''

'''
	import sphene.modules.law_dictionary as law_dictionary

	#
	#	contigencies
	#
	law_dictionary.check (
		allow_extra_fields = False,
		
		laws = {
			"directory": {
				"required": True,
				
				#
				#	if "required" == False and does not have "directory",
				#	then either:
				#		( ) use the value provided
				#		( ) call the function
				#
				"contingency": retrieve_directory
			}
		},
		dictionary = {}
	)

	def retrieve_directory ():
		return os.path.dirname (
			os.path.abspath ((inspect.stack ()[1]) [1])
		)

	law_dictionary.check (	
		laws = {
			"directory": {
				"required": false,
				"contingency": retrieve_directory,
				"type": str
			}
		},
		dictionary = {}
	)
'''

import rich
import types

def problem (string):
	raise Exception (string)
	


def check (
	allow_extra_fields = False,
	
	laws = {},
	dictionary = {},
	
	problem = problem
):
	if (allow_extra_fields != True):
		for label in dictionary:
			if (label not in laws):
				return problem (f'The extra label "{ label }" was not found in the laws.')
			
	for law_label in laws:	
		law_label_params = laws [ law_label ]
	
		if ("required" in law_label_params):
			required = law_label_params [ "required" ]
		else:
			required = True
	
		if (required == True):
			if (law_label not in dictionary):
				return problem (f'The label "{ law_label }" was not found in the laws.')
			
		else:	
			if ("contingency" in law_label_params):
				contingency = law_label_params [ "contingency" ]
				#print ('has contingency', contingency)
				
				if (type (contingency) == types.FunctionType):
					dictionary [ law_label ] = contingency ();
				else:
					dictionary [ law_label ] = contingency;

			else:
				return problem (
					''.join ([
						f'Non-required laws must have a contingency.',
						f'"{ law_label }" does not have a contingency'
					])
				)

		'''
			After the required piece, the definition can be
			100% determined.
		'''
		dictionary_definition = dictionary [ law_label ];
		
		if ("type" in law_label_params):
			label_type = law_label_params [ "type" ]
			
			if (type (dictionary [ law_label ]) != label_type):
				return problem (f'Defintion "{ dictionary [ law_label ] }" is not type "{ label_type }".')
		
		
		if ("allow" in law_label_params):
			label_allow = law_label_params [ "allow" ]
		
			if (type (label_allow) == types.FunctionType):
				allowed = label_allow ();
			else:
				allowed = label_allow
				
			if (dictionary_definition not in allowed):
				return problem (f'Defintion "{ dictionary_definition }" is not allowed.')
		
		#print (law_label_params)
		
	return;