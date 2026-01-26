
# ordered items
# unchangeable items
# allow duplicates

tupConstruct = tuple(('a', 'b', 'c', 'c'))

tup = ('a' ,'b', 'c')


# accessing it is the same as list using slicing or extract



# but changing elements value is different

# tuple -> list -> modefy -> tuple
# meaning all of list methods we can use from a derived tuple
newLs = list(tupConstruct)
newLs[0] = 'sdfasfdasdf'
tupConstruct = tuple(newLs)


print(tupConstruct)



# unpack | destructure

def getAandB(tup) : 
    (sdfasfdasdf, b, *other) = tup # *other collect the rest of them
    return sdfasfdasdf, b


print(getAandB(tupConstruct))



# loops -> since tuples can be read we can use ordinary loopings, like for, comprehension, while and range




# join tuples 


nextTuples = ('hello', 'world')



def getAllTup(tup1, tup2) :
    return tup1 + tup2


# print(getAllTup(tupConstruct, nextTuples))