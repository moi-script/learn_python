x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x), type(y), type(z)) # <class 'str'> <class 'int'> <class 'float'>


def userType(val) :
    return int(val) + 10

# print(userType(input())) # terminal auto accept value as string, so 10 is enough not "10";


def userType2(val) :
    toFloat = float(val)
    toInt = int(toFloat)
    
    print("Float: ", toFloat)
    print("Integer: ", toInt)
    


# userType2(input())


def userType3(val) :
    toInt = int(val)
    toFloat = float(val)
    toStr = str(val)
    
    print("Integer: ", toInt, type(toInt))
    print("Float: ", toFloat, type(toFloat))
    print("String: ", toStr, type(toStr))
    

# userType3(input())
    
    
    
# more about safe casting 



    # try:
    #     x = int(input("Please enter a number: "))
    #     break
    # except ValueError:
    #     print("Oops!  That was no valid number.  Try again...")
    
    
def userType4(val):
     try :
         toInt = int(val)
         print("Valid integer: ",toInt)
     except ValueError as e : 
         print("Unable to convert to integer the input is Invalid number", e)

# userType4(input())


def userType5(val) :
    if "." in val :
        print("Detected float : ", float(val))
    else :
        print("Detected Integer", int(val))

# userType5(input())



def userType6(val) :
    try :
        if "." not in  val :
            print("Detected Integer :", int(val))
        else :
            print("Detected Float", float(val))
    except ValueError as e :
        print("Invalid Input", e)
            
        
# userType6(input())


            
# 0 in python boolean is True, not in js though
def userType7(val) :
    b = bool(val)
    print("Boolean value : ", b)
    
# userType7(input())





def userType8(val) :
    l = val.lower()
    try :
        if l in ["true", "yes", "1"]:
            print("Boolean value : ", True) 
        elif l in ["false", 'no', "0"]:
            print("Boolean value :", False)
        else : 
            raise ValueError("Invalid input", val)
    except ValueError as e :
        print("Error occured : ", e.args)

# userType8(input())



# print(int(10.6))



def userType9(val):
    l = val.lower()

    # 1. Boolean first (manual mapping)
    if l in ["true", "yes", "1"]:
        print("Boolean:", True)
        return
    elif l in ["false", "no", "0"]:
        print("Boolean:", False)
        return

    # 2. Try integer
    try:
        num = int(val)
        print("Integer:", num)
        return
    except ValueError:
        pass

    # 3. Try float
    try:
        num = float(val)
        print("Float:", num)
        return
    except ValueError:
        pass

    # 4. Fallback
    print("Invalid input")

# userType9(input())




def test(val) :
    try :
        n = int(val)
        print("Integer : ", n)
        return
    except ValueError:
        pass
    
    try :
        n = float(val) 
        print("Float :", n)
        return
    except ValueError :
        pass
    
    print("Invalid input")
        
test(input())