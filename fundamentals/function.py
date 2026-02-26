


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







# The LEGB Rule
globalsVar = 1000

def testGlobalScopeConfig() :
    global globalsVar
    globalsVar = 100
    
    
print("before ::", globalsVar)  




testGlobalScopeConfig() # global declaration allows variables to be config

print("After :: ", globalsVar)
    
    
    
    
x = "global test"

def outerFunc() :
    x = "enclosing"
    
    def inner() :
        nonlocal x
        print("Inner function --> ", x)
    inner()
    print("Outer --> ", x)
    
    
outerFunc()

print("Global x")





# decorators



def caller(funcArg) :
    def returnFn() :
        return funcArg().lower()
    
    return returnFn



@caller # @ -> makes a python decorate when it specifically return an initial function references 
def funcArg() :
    return "HELLO WORLD"

print(funcArg())





# dict example



colors = {
    "col" : "white"
}

def setColor(changeCol) :
    def color(color) :
        global colors
        colors["col"] = changeCol(color)
        return colors
    return color


@setColor # this is a reference function so calling it like setColor() => returning the color function 
def changeColor(newColor) :
    return newColor
# print(changeColor("red"))





# argument with decorator


def testArgDecorator(value) :
    def testArgDecorator(fn) :
        def inner() :
            if(value == "hello") :
                return fn() + value
        return inner
    
    return testArgDecorator


@testArgDecorator("hello")
def init() :
    return "World"


print(init())

def printColors() :
    global colors
    colors = {"col" : "blue"} # this creates   new local variable
    print(colors)


# printColors()

# print(colors)



# lambda 


x = lambda a, b : a + b # like arrow function in js
print(x(10, 20))    



# doing lambda with list 


listNums = [1, 2, 3, 4, 5]

# alternative
def sums(a) :
    return a + a 

# lambda a : a + a
sums = list(map(sums, listNums))

print(sums)





# using range-> range(start, stop, step)

for i in range(len(sums)) :
    print(sums[i])  





# iterators 


tups = ("test1", "test2", "test3")

myTupsI = iter(tups)


def iters() :
    for i in range(len(tups)) :
        print(next(myTupsI))

iters()