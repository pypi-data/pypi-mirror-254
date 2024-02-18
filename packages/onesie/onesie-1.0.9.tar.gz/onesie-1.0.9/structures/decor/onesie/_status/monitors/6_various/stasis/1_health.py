



def check_1 ():
	print ("check 1")


def check_2 ():
	print ("check 2")
	raise Exception ("NOT 100%")


checks = {
	"check 1": check_1,
	"check 2": check_2,
	"check 3": lambda : (),
	"check 4": lambda : (),
	"check 5": lambda : (),
	"check 6": lambda : (),
	"check 7": lambda : (),
	"check 8": lambda : ()
}