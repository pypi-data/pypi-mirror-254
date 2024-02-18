


def check_1 ():
	import pathlib
	from os.path import dirname, join, normpath
	import os.path

	this_folder = pathlib.Path (__file__).parent.resolve ()
	this_txt = normpath (join (this_folder, f"998.txt"))
	assert (os.path.isfile (this_txt) == False) 

	fp = open (this_txt, "w")
	fp.write ("998")
	fp.close ()

	return


checks = {
	"check 1": check_1
}

