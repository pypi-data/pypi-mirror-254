



import MODULE_1

def check_1 ():
	print ("check 1")
	MODULE_1.FUNCTION ()
	
	# raise Exception ()
	
	return;
	
def check_2 ():
	print ("check 2")
	
	# raise Exception ()
	
	return;
	
def check_3 ():
	
	raise Exception ("NOT 100%")
	
	return;

checks = {
	"check 1": check_1,
	"check 2": check_2,
	"check 3": check_3
}