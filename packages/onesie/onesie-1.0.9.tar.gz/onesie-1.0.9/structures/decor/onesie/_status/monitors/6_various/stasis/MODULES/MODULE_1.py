

def START (END_OF_STRING_IS):
	print ("MODULE 1", __file__)

	assert (
		END_OF_STRING_IS (__file__, "6/MODULES/MODULE_1.py") ==
		True
	)

	return;