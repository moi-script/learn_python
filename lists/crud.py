# List items are ordered, changeable, and allow duplicate values.

# indexing
# negative indexing
# range of index
# in operator in list


testCases = ["test1", "test2", 'test3', "test4"]



# update item in the list

# by index

def changeByIndex(l, index, newValue) :
     l[index] = index
     return l

def changeRangeIndex(l, start, end) -> list : 
    l[start:end] = ["newTest1", "newTest2"]
    return l

def changeByInsert(l : list, newValue) -> list : 
    l.insert(len(l), newValue) # (insert at index , value to insert)
    return l

# print(changeByInsert(testCases, [10, 20]))







# for create items


def appendBy(l : list, newValue) -> list : 
    l.append(newValue)
    return l


typesList = list | tuple | dict
def addTwoList(prevList : typesList , newList : typesList) ->  list :
    prevList.extend(newList)
    return prevList

# print(addTwoList(testCases, [1, 2, 3, 4]))







# delete | remove items 

def removeMethod(l : list, value) -> list :
    l.remove(value); return l
    
# print(removeMethod(testCases, "test1"))
    
    
def removeTricks(l : list, value) -> list:
    return [x for x in l if x != value]

# print(removeTricks(testCases, "test1"))

def removeByPop(l : list, index) -> list : 
    return l, l.pop(index)


def removeByDelete(l : list, index) -> list : 
    del l[index]; return l
    
    
def removeDeleteAll(l : list) -> None: 
    del l; return None # when delete, it severed the reference to class list 
    
# print(removeDeleteAll(testCases))

def removeByClear(l : list) -> list[any] :
    l.clear(); return l 

# print(removeByClear(testCases))







# read items 



def readListItems(l : list) :
    for x in l :
        print(x)
        
# readListItems(testCases)


def readListByRange(l : list) : 
    for i in range(len(l)) : # much more controlled
        print(l[i])

# readListByRange(testCases)

def readByWhileLoop(l : list ) :
    i =0
    while i < len(l) :
        print(l[i])
        i = i + 1
        
# readByWhileLoop(testCases)

def readByComprehension(l : list) :
    [print(x)  for x in l]
    
# readByComprehension(testCases)






