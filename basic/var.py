# comments 
# print("hello world"); test consoles 
#  python myfile.py running files 

# starting 

# indentation
# from typing import List, Tuple

# test = 10
# if test == 10:
#     print("10 is correct")






n = 100 # now int class is pointing to n 
p = 200

# print(id(n)) # 140709863239688
# print(id(p)) # 140709863242888



def s(arg) :
    try :
        if isinstance(arg, tuple) :
            return type(arg)
        
        raise ValueError("Error")
    except ValueError as e :
        print("Unable to accept invalid argument", e)
# using hints

# value : s(10) = ("a", "b", "c") # working but be aware 
value : tuple = ("a", "b", "c") # just do this  

# print(value)

person : dict[str, str] = {
    "1" : "Juan",
    "2" : "John",
    "3" : "Smith"
}

info : dict[int, tuple] = {
    10 :  (1, 2, 3, 4, 5),
    20 :  (1, 2, 3, 4, 5),
    30 :  (1, 2, 3, 4, 5),
    
}
# print(person)

def printlist(dic) :
    for x in dic :
        print(dic[x])

# printlist(info)


listed : list[tuple[str, str, str]] = [ 
    ("10", "20", "30"),
    ("40", "50", "60"),
    ("70", "80", "90"),
    
]

# print(listed)





# parallel way 

x = y = z = 1000

# print(x, y, z)




 # Iterable Unpacking

personList = ("John Smith", "Lyr", "John")
# print(personList[0], personList[1], personList[2]) 

# destructure
p1, p2, p3 = personList




# swap
p1, p2  = p2, p1
print(p1, p2)


# expression 

def loopInput() :
    ins = input("Enter some text")
    while ins != "done" :
        print(ins)
        ins = input("Enter some text ")
        
        
# loopInput()


# Global scope
global_variable = "global"

def outer_func():
    # Nonlocal scope
    nonlocal_variable = "nonlocal"
    def inner_func():
        # Local scope
        local_variable = "local"
        print(f"Hi from the '{local_variable}' scope!")
        print(f"Hi from the '{nonlocal_variable}' scope!")
        print(f"Hi from the '{global_variable}' scope!")
    inner_func()
    
# test some fun 
def dynamicText(arg) :
    list = {}
    for i in range(10) :
        list[i] = f"Dynamic context game {arg}" 
    
    return list
        
dynamicTextList = dynamicText(input("Enter text : "))

for inputList in  dynamicTextList:
    print(dynamicTextList[inputList])