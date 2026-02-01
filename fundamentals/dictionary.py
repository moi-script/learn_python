
test = {
    "a" : "value a",
    "b" : "value b",
    "c" : "value c"
}

def valueList(dict) : 
    for x in dict.values() :
        print(x)


valueList(test)



def loopItems (list) :
    for x, y in list.items() : 
        print(x, y)



loopItems(test)