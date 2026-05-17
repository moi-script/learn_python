import  string
numberList = [2, 3, 4, 5, 6, 7]
numberList2 = [2, 10, 20, 3]
def get_even_numbers(nums : list[int]) -> list[int] :
    return [x for x in nums if x % 2 == 0]


# print(get_even_numbers([2, 3, 4, 5, 6, 7]))

def square_even_number_v1(nums : list[int]) -> list[int] :
    return [x * x for x in get_even_numbers(nums)]


def square_even_number_v2(nums : list[int]) -> list[int] :
    return [x * x for x in nums if x % 2 == 0]

# print(square_even_number_v2(numberList))

def common_elements(nums : list[int], nums2 : list[int]) -> list[int]:
    return [x for x in nums if x in nums2] 
# print(common_elements(numberList, numberList2))



# Start with the list: colors = ["red", "blue", "green", "yellow", "purple"].

# Step 1: Change the range from index 1 to 3 (exclusive of 3) to the values ["cyan", "magenta"].  

# Step 2: Use the .insert() method to place the string "white" at the very end of the list 
# by calculating the index dynamically using len().  

# Step 3: Use a single command to remove the item at index 0 and store it in a variable named removed_item.


colors = ["red", "blue", "green", "yellow", "purple"]


def colorShift(colors : list[str]) ->  dict[list[str], str] : 
    colors[1:3] = ["cyan", "magenta"]
    colors.insert(len(colors), "white")
    
    removeItem = colors.pop(0)
    
    return {
        "colors" : colors,
        "poppedItem" : removeItem
    }
    
    
# print(colorShift(colors))
# the function should filter the type of value bases on the dictionary 
schema = {
    "number" : int,
    "string" : str
}

def strictBasedFiltering(data : list, schema : dict) :
    return [x for x in data if isinstance(x, tuple(schema.values())) and not isinstance(x, bool)] # this can't determined the boolean value

# print(strictBasedFiltering([10, 20, "hello world", 3.14, False, {},()], schema))



# sort() -> returns key for 0 = numbers, 1 = string | text


# brute force for solving sorting of number and integer at once 
def numerical(n) -> dict : 
    def closeError(x) :
        isNum = False
        try :
            isNum = isinstance(int(x), int)
            
        except ValueError :
             isNum = False
        
        return isNum 
             
    nums = [int(x) for x in n if closeError(x)]
    nums.sort()
    return {
        "sorted" : [str(x) for x in nums],
        "end" : len(nums),
        "start" : 0
    }

def advanceSorting_v1(data : list) -> list[str | int] | None :
    data.sort(key= str.lower)
    strNums, end, start = numerical(data).values()
    
    data[start:end] = strNums
    
    return data


def advanceSorting_v2(data : list) -> list[str | int] :
    def sortKey (item) :
        isNums = item.isdigit()
        
        if isNums :
            return (0, int(item))
        else :
            return (1, item.lower())
        
    data.sort(key=sortKey)
    return data

# print(advanceSorting_v2(["Banana", "10", "apple", "2", "Cherry"]))




# cleaning user input

def cleanUserData_v1(data : list) -> list :
    def  remove_short(n) :
        
        c = cleanWhiteSpace(n)
        if len(c) < 3 :
            return False
        else :
            return True
    
    def cleanWhiteSpace(n) :
        return ''.join(char for char in n if char not in string.whitespace)
    
    
    return [cleanWhiteSpace(x).lower().capitalize() for x in data if remove_short(x)]
        
# print(cleanUserData_v1(["  aLiCe ", "bo", "   cHaRliE  ", "ed", "DAVE", " x "]))
# print(cleanUserData(["  aLiCe ", "bo", "   cHaRliE  ", "ed", "DAVE", " x "]))


# clean version  
def  cleanUserData_v2(data : list) -> list :
    return [x.strip().title() for x in data if len(x.strip() >=3)]









# You are building a basic RPG inventory system. The player has their current 
# inventory, and they just opened a treasure chest containing new items.

# Your Task:
# Write a function loot_chest(inventory: list, chest: list) that performs the following steps in order:

# Join: Combine the inventory list and the chest list into a single new list.
# You must use the unpacking operator (*) to do this (as seen in your join.py file).

# Filter (Delete): The player immediately drinks all the "Potion" items. 
# Use a list comprehension (like your removeTricks from crud.py) to remove every instance of "Potion" from the combined list.

# Sort: Sort the remaining items alphabetically.

# Return the final list.


def loot_chest(inventory : list, chest : list) :
    merge = [*inventory, *chest]
    noPotionList = [x for x in merge if x != "Potion"]
    noPotionList.sort(key=str.lower)
    return noPotionList

# print(loot_chest(["Sword", "Shield", "Potion"], ["Gold", "Potion", "Map", "Boots"]))
    
    
    


def flatten_grid(matrix : list) :
    # return [x[:] for x in matrix]
    # nest = []
    # for x in matrix :
    #     for y in x :
    #         nest.append(y)
        
    # return [x for x in nest]
    
    # "Left-to-Right Rule".
    # [ (item) (outer loop) (inner loop) ]
    return [y for x in matrix for y in x]

        

# print(flatten_grid([
#     ["A1", "A2", "A3"],
#     ["B1", "B2", "B3"],
#     ["C1", "C2", "C3"]
# ]))



# [A if condition else B for item in list])
def transform_numbers(numbers : list) :
    
    return [x//2 if x % 2 == 0 else x * 3 for x in numbers]

# print(transform_numbers([1, 2, 3, 4, 5, 6]))



products = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# 2 pages
# 4 pages
 

 
# print(firstPage)
# print(secondPage)


def get_page_v1(data : list, page : int, page_size : int) :
    l = len(data)
    
    all_value = []
    data_page_id = round(l/page_size)
    data_page_value = []
    
        
    for x in range(l) :
        if (x + 1) % data_page_id == 0 :
            data_page_value.append(data[x])
            all_value.append(data_page_value)
            data_page_value = []
            
            
        else : 
            data_page_value.append(data[x])
        
            
    all_value.append(data_page_value)
    
            
    
    return all_value[page]
    
    
    
    
# def get_page_v2(data : list, page : int, page_size) :
    

# print(get_page(products, page=2, page_size=3))


