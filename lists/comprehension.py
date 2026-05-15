
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


newList = []

def populateNewList(l : list, newList) -> list :
    for x in l :
        if "a" in x :
            newList.append(x)
            
            
    return newList

# print(populateNewList(fruits, newList))

# updated 


def detectInstances(l : list) -> tuple :
    return tuple([type(x) for x in l])



def populateNewListShort(l : list) -> list[str] :
    return [x for x in l if "a" in x]


print(detectInstances(fruits))


schema = {
    "text": str,
    "number": int,
    "flag": bool,
    "decimal": float
}

def filter_by_schema(data: list, schema: dict) -> list:
    return [x for x in data if isinstance(x, detectInstances(data))]

print(filter_by_schema(fruits, schema))