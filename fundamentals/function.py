


# try to config ref from function 

thisList = {
    "a" : "value a",
    "b" : "value b",
    "c" : "value c"

}



# function could update the reference via arguments
def change(list) :

    newCopy = list.copy()
    newCopy.update({"a" : "new value from a"})
    return newCopy


print(change(thisList))




# * args allows function any number of positional arguments, 


# **kargs -> keyword arguments, it becomes dictionary and can be access using their keys 





# *args
def testArgs(*args) :
    for ar in args :
        print(ar)

testArgs("a", "b", "c", "d")




def testKargs(**test) :
    for key, value in test.items() :
        print(key)

            
testKargs(name="John", age=30)