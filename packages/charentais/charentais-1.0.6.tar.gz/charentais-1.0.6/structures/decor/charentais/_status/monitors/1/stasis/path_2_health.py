

import time

def check_1 ():
	print ("check 1")
	
	#time.sleep (2)
	#print ("check 1 AFTER SLEEP")
	
	# raise Exception ()
	
	return;
	
def check_2 ():
	print ("check 2")
	
	# raise Exception ()
	
	return;
	


checks = {
	"check 1": check_1,
	"check 2": check_2
}