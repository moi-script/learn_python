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

schema = {
    "number" : int,
    "string" : str
}


def strictBasedFiltering(data : list, schema : dict) :
    return [x for x in data if isinstance(x, tuple(schema.values())) and not isinstance(x, bool)] # this can't determined the boolean value

# print(strictBasedFiltering([10, 20, "hello world", 3.14, False, {},()], schema))



# sort() -> returns key for 0 = numbers, 1 = string | text


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

print(advanceSorting_v2(["Banana", "10", "apple", "2", "Cherry"]))
