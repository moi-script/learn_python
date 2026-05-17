import json

# ordered or unordered base on version, ordered base are version3.7
# changeable
# not allow duplicates 



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # re assigned
}

thisdict2 = dict(name = "John", age = 36, country = "Norway")

# print(len(thisdict2))




# access dictionary 


brand = thisdict["brand"]
model = thisdict["model"]
year = thisdict["year"]

def getYear(data : dict, props : str) -> str :
    return data.get(props) # similar to data[props]

def getBrandKeys(data : dict) -> list :
    return list(data.keys())

def getBrandValues(data : dict) -> list :
    return list(data.values())

# print(brand, model, year)
# print(getYear(thisdict, "brand"))
# print(getBrandValues(thisdict))
# print(type(getBrandKeys(thisdict)))



# .items() -> this return a dict items that is a key / value pair of tuples

def getBrandItems(data : dict) -> tuple :
    return tuple(data.items()) 

# loopBrandItems(thisdict)
# print(type(getBrandItems(thisdict))) # we can convert back to dict()

def isKeyExist(data : dict, key : str ) -> bool :
    if key in data :
        return True
    return False


# print(isKeyExist(thisdict, "sdfsdf"))


# update 
def updateBrand(data : dict, key : str, value : any) -> dict :
    return data.update({key : value})



# add item 

def addItemBrand(data : dict, key, value) -> dict :
     data[key] = value; return data

# print(addItemBrand(thisdict, "newhehhe", 1000))
    

def removeItemBrand(data : dict, key) -> dict :
    data.pop(key); return data
    
    
    
def deleteBrandKey(data : dict, key) -> dict :
    del data[key]; return data
    
# print(deleteBrandKey(thisdict, "model"))

def deleteAllBrandKey(data : dict) -> None :
    del data; return None
    

# print(deleteAllBrandKey(thisdict))

def emptyBrand(data : dict) -> dict :
    data.clear(); return data
    
# print(emptyBrand(thisdict))



# loop print values
def loopBrand(data : dict) : 
    for x in data :
        print(data.get(x)) # get the value, x -> property 


def loopBrandValues(data : dict) :
    for x in data.values():
        print(x)
        
# loopBrandValues(thisdict)

def loopBrandItemsAll(data : dict) :
    for x, y in data.items() :
        print(x, y)
    
    
def loopBrandKey(data : dict) :
    for x in data.keys() : # we can just directly use dictionary, it auto saves the key in x
        print(x) 
# loopBrandItems(thisdict)




# copy dictionay 


def copyBrand(data : dict) -> dict :
    return data.copy()     # we cannot, thisdict2 = thisdict  

# print(copyBrand(thisdict) == thisdict)

def copyBrandByConstructor(data : dict) -> dict :
    return dict(data)

# print(copyBrandByConstructor(thisdict) == thisdict)



# nested dictionary 
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


def printNestedObject(family : dict) : 
    for key, value in family.items() :
        # print(key, value)
        for v in value :
            print(v)
        
# printNestedObject(myfamily)

def printNestObjectV2(family : dict) :
    # return [y for x in matrix for y in x]
        
    return [v for _, value in family.items() for v  in value]
    
# print(printNestObjectV2(myfamily))





def convertToJson(data : dict) -> str :
    return json.dumps(data)


# familyJson = json.dumps(thisdict)
# print(convertToJson(thisdict))


# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null


# print(type(json.dumps(dict(key="person1", value="juan")))) # str
# print((json.dumps(['hello', 'world']))) # str
# print(type(json.dumps(10)))# str

# Python objects are converted into the JSON (JavaScript) equivalent:


# From Python -> JS object specialty 
x = {
  "name": "John",
  "age": 30, 
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# print(json.dumps(x))


# indents
def organizedJsonOutput(data : dict) -> str :
    return json.dumps(data, indent=4) # makes indentation in string format

# print(organizedJsonOutput(x))


# separator -> beware of using separator, it might affect the future parsing of json to object

def separatorJsonOutput(data : dict) -> str : 
    return json.dumps(data, indent=4, separators=(". ,"," = ")) # arg1 = separator, arg2 = equal

# print(separatorJsonOutput(x))

def parseJSON(data : str) -> dict :
    return json.loads(data)

print(parseJSON(organizedJsonOutput(x)))