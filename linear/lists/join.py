list1 = [10, 20, 30, 40, 50]
list2 = [30, 10, 1, 2]

# print(list1 + list2)

def addByLoopsComprehension(list1, list2) : 
    return [x for x in list2] + [y for y in list1]

# print(addByLoopsComprehension(list1, list2))

def addByLoopsManual (list1, list2) : 
    for x in list1 :
        list2.append(x)
        
def addByUnpack(list1, list2) :
    return [*list1, *list2]        

print(addByUnpack(list1, list2))
        
# print(addByLoops(list1, list2))