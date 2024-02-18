

def START (end_of_string_is):
	print ("MODULE 1", __file__)

	assert (
		end_of_string_is (__file__, "stasis/MODULES/MODULE_1.py") ==
		True
	)

	return;