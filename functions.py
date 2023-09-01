#functions

#basic function
def func_01():
    print("Hello World!")
func_01()
#Key word Arguments
def func_01(fname,lname):
    print("hello",fname,lname)
func_01(lname="Vijayaraj",fname="Vidhyasri")

#Arguments
def func_01(fname):
    print("hello",fname)
func_01("Venky")

#multiple Aruguments
def func_01(fname,lname):
    print("Hello",fname,lname)
func_01("Venkata","krishana")

#Arbitary
def func_01(*tname):
    print(tname[2])
func_01("vidhya","sri","uma")

#Arbitary keyword argument
def func_01(**greet):
    print("Hello",greet["key2"])
func_01(key1="vidhya",key2="venky")


#Default parameter value
def func_01(tname="dog"):
    print(tname)
func_01("hen")
func_01("duck")
func_01()

