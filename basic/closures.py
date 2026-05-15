


def checkList() :
    list = []
    
    def appendList(i) :
        list.append(i)
        
    return {
        "append" : appendList,
        "getValue" : list
    }
    

result = checkList() # saved the local scope as closure : 
append, getValue = [result["append"], result["getValue"]]

append(1000)
# print(getValue)


# lamda expression --> anonymous function in javascript

def outer_func():
     name = "Pythonista"
     return lambda: print(f"Hello, {name}!")


greeter = outer_func()
greeter()

# Hello, Pythonista!



def outer_func2  () :
    name = "test"
    
    return lambda a : print(f"This is {name + a}")

t = outer_func2()

t("another")