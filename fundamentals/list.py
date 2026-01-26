

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# L -> OC duplicate
# T -> OUC duplicate
# S -> UDUCUX -> unordered, unchangeable, unindex, no duplicate
# D -> OC no duplicate



# []




ls = ["a", "b", "c", "d", "e", "f"]

# accessing items 
getbegin = ls[:3] # a, b, c
getend = ls[3:] # d, e, f
getmid = ls[2:4] # c, d
# print(getbegin)
# print(getend)
# print(getmid)


def checkItem(list) :
    return "a" in list

# print(checkItem(ls))

ls[:3] = [1, 2, 3]
ls[3:] = [4, 5, 6]

# insert(pos, element)
# print(ls)

# print(ls)




# add list items 

ls.append('new value')
ls.insert(2, "hello world")
ls.extend(["hh", "a", "w"])

# print(ls)

# remove list items


ls.remove(1) # remove(value)
ls.pop(2) # remove(pos) | remove() -> last item
# ls.clear()

# print(ls)





# loops in the list 


def printList(list) : 
    for item in list :
        print(item) 

def printRangeList(list) :
    for i in range(len(list)) :
        print(list[i])

def printWhilelist(list) : 
    i = 0
    while i < len(list) : 
        print(list[i])
        i += 1


def printForExpression(list) :
    [print(x) for x in list]

printForExpression(ls)




# List compression  -> makes a shorter syntax for loops 


aplb = ["a", "b", "c", "d", "e", "f"]
newLs = [x for x in aplb if "hello world" in x]
newList = [x for x in range(10) if x < 5]
toUpper = [x.upper() for x in aplb]



def toUpperList(list) :
    toUpper = [x.upper() for x in list]
    print(toUpper)

def changeToHi(list) :
    hi = ['hi' for x in list if 'a' in x]
    print(hi)


def changeElement(list) : 
   newlist = [x if x != "b" else "g" for x in list] # if this x is equal to b this will go to else which is g
   print(newlist)
# print(toUpper)

changeElement(aplb)





# sorting 


def toALphaNumeric(list) :
    newList = list.copy()
    newList.sort(reverse = True)
    print(newList)


toALphaNumeric(aplb)