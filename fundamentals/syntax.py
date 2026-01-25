
# variables 

x = 1000
name = "John Doe"


# different values
a, b, c = 'a', 'b', 'c'

# print(a, b, c)

# similar value in multi variable

d = e = f = "a"
# print(d, e, f)


# global variables

testValue = 'all global value'

def testPrint() : 
     print("This is test " + testValue )

# print(testPrint())




def closures(param1): 
    return lambda  : param1 + 'a'



acceptGlobal = closures("For param1")

# print("This is the global closures :: " + globalClosures)
# print(acceptGlobal())
# print(acceptGlobal())
# print(acceptGlobal())
# print(acceptGlobal())



printHello = lambda : "hello world"


# print(printHello())




# data types 

# Text type -> str
# Numeric types -> int, float, complex
# sequence types -> list, tuples, range
    # list -> x = ["apple", "banana", "cherry"]
    # tuple -> x = ("apple", "banana", "cherry")
    # range -> x = range(6)


# Mapping types -> dict
    # dict -> x = {"name" : "John", "age" : 36}
    
# Set types -> set, frozenset
    # set -> x = {"apple", "banana", "cherry"}
    # frozenset -> x = frozenset({"apple", "banana", "cherry"}) 

# Boolean types -> bool
    # bool -> True | False

# Binary types -> bytes, bytearray, memoryview

    # bytes -> x = b"Hello worl"
    # bytearray -> x = bytearray(5)
    # memoryview -> x = memoryview(bytes(5))
    # None -> x = None    
# None Types -> NoneType
# Function types -> lamba | def



def testType() : 
    pass
 
t = lambda : "type"
r = 10
print(type(testType), type(r))


print(memoryview(b"5"))


# loops

def initMemory(memory) : 
    # using .decode("utf-8") to converts bytes -> str
    textFromMemory = memory.decode('utf')
    for (i, m) in enumerate(textFromMemory, start=1) :
        print(m) # who to convert the bytes to origin value


# initMemory(bytearray(b"Hello world"))




def testLoopRange() : 

    ls = [10, 20, 30, 40, 50]

    for i in range(0, len(ls)) : # range(start, stop, step) defaults range(10) 0 -> 10  
        print(ls[i])


# testLoopRange()


def shortCut() :
    print(list(range(20))) # auto create a list of certain range 
    print(list(range(2, 20)))
    print(list(range(1, 100, 2)))


# shortCut()


def slices() : 
    r = range(1, 10, 2) # r = range(1, 10, 2)

    toLoops = r[:10] # extact range object with range(0, 10)
    
    for (i) in toLoops :
        print(i)

    # print(r[2])
    # print(r[:10])


# slices()



def tryWhileLoops() : 
    i = 10

    while ( i > 1) :
        i -= 1

        if(i == 3) :
            break
        
        print(i)


# tryWhileLoops()


# recusive -> the default recursive is 1000 we can adjust this my 
# import sys
# sys.setrecursionlimit(2000)

def factorials(n) :
    if n == 0 or n == 1 :  # base case 
        return 1
    else : # recursive case 
        return n * factorials(n-1)

# print(factorials(3))

def fibon(n) : 
    if n <= 1 :
        return 1
    else : 
        return fibon(n-1) + fibon(n-2)

# print(fibon(10))


def recursiveList(numbers) : 
    if len(numbers) == 0 :
        return 0
    else : # adding first index all together while popping out it
        return  numbers[0] + recursiveList(numbers[1:])

tryLs = [10, 30, 50, 10]
# print(recursiveList(tryLs))



def find_max(numbers) :
    print(numbers)

    if len(numbers) == 1 :
        print('Trigger', numbers)
        return numbers[0]
    
    else : 
        max = find_max(numbers[1:])
        print(" max val", max)
        return numbers[0] if numbers[0] > max else max


mxlist = [2000, 20, 1000, 1, 34]

# print(find_max(mxlist))

# static 
def generateList() : 
    yield 1
    yield 2
    yield 3
    yield 4


def printGeneratedList(list) :
    for val in list :
        print(val)

# dynamic list generation 
def generateListDynamic(n) :
    index =0

    while index < n : 
        yield index + 1
        index += 1

# printGeneratedList(generateListDynamic(20))



# saving memory using generators 

def largeSequence(n) :
    for i in range(n) :
        yield i

# gen = largeSequence(1000000)


# print(next(gen))
# print(next(gen))
# print(next(gen))



# creates generator
genExp = ( (x * x) for x in range(20))

print(list(genExp))


































# conditions 

# if (5 > 2):
#  print("Five is greater than two!") 

# if 5 > 2:
#         print("Five is greater than two!") 





# output 
# print() function ends with a new line but using ,end = "" as 2nd param it will not 
# print("Hello, Today I am learning python fundamentals", end = "test")



"""
Multiple comments attempt
test 
"""


