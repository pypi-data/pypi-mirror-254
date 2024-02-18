

'''
	This checks if a partial string
	is at the end of another string.
'''
def end_of_string_is (STRING, PARTIAL):
	try:
		INDEX = STRING.index (PARTIAL)

		if (len (STRING) == (INDEX + len (PARTIAL))):
			return True
			
	except Exception:
		pass

	return False

import MODULE_1

def check_1 ():
	print ("__file__ check", __file__)
	
	assert (
		end_of_string_is (__file__, "stasis/1_health.py") ==
		True
	)
	
	MODULE_1.START (end_of_string_is)

	return;


checks = {
	"CAN ACCESS THE __file__ VARIABLE": check_1
}