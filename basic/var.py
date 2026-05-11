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

print(id(n)) # 140709863239688
print(id(p)) # 140709863242888



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

print(listed)