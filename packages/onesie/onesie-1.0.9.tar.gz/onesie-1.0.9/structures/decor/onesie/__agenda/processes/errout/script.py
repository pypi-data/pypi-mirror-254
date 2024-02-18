


import time

episode = 1
def routine ():
	global episode;

	print ('routine', episode)
	#print (b'asdf')
	
	episode += 1
	
	time.sleep (1)
	
	if (episode <= 5):	
		routine ()
	
routine ()