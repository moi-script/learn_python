
# Primitive Types
# Collection Types
# Binary Types
# Null
# Function types 
# Object oriented type
# iterator type

def testFn() :
    print("Test function")
    
# print(type((x for x in range(5))))



# Memoize 

def memoize(function) :
    cache = {}
    def closure(number) :
        if number not in cache :
            cache[number] = function(number)
        return cache[number]
    
    return closure 
 

# counter state 

def counter () :
    count = 0
    def add() :
        nonlocal count # this ensure to not create a new local variable inside inner function. 
        count += 1
    
        return count
    return add

resultValue = counter()

# print(resultValue())
# print(resultValue())
# print(resultValue())
