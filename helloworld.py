print "Hello, World!"
def get_name():
	name= raw_input ('What is your name?')
	return name

def greeting():
	name = get_name()
	greeting= "Hey, there" " " + name + "."
	
	print greeting 

greeting()

