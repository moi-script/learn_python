
from lists.crud import changeByIndex 

# ordered 
# unchangeable 
# allow duplicates


# tuples test 

tups = ("test1",) # should at alteast had ','
# print(type(tups))


# create 
tupByConstructor = tuple(("test1", "test2", "test3"))
tupByInitial = ("test2", "test3", "test4")

# print(tup2)


def createTupsByEnumerate() :
    return tuple([(i, value) for i, value in enumerate([10, 20, 30])])
        
# print(createTupsByEnumerate())

# access tuples 


# init data test

data = tuple([f"test value {x}" for x in range(30)])
# print(data)

def getTupsItemByIndex(data : tuple, index) :
    return data[index]
      
# print(getTupsItemByIndex(("test1", "test2", "test3"), -1)) #  negative index starting with the last

# slicing same as list 
def getTupsItemByRange(data : tuple, start : int, end:int) :
    return data[start:end]

# print(getTupsItemByRange(data, 3, 10))




# update tuples -> tuples is immutable so we need to convert this first into list before config


list_data = list(data) # data set of tuples are not list
list_mutate = changeByIndex(list_data, 10, "Hello world")

def is_mutated(list_data : list) -> bool :
    for x in list_data :
        if x == "Hello world" :
            return True
        
    return False

def list_to_tuples(list_data : list) -> tuple | None :
    if is_mutated(list_data) :
        return tuple(list_data)
    
    return None  
    
# print(list_mutate)
# running this in the tuple/crud.py -> wont work since it cannot see other  file siblings 
# python -m tuple.crud



