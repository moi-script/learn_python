


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


