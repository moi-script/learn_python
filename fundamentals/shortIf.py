a = 100
b = 200


print("A") if a > b else print("B")



def returnVal() :
    return a if a < b else b


print(returnVal())