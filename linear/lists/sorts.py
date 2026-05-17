thislist = ["orange", "mango", "kiwi", "pineapple", "Banana"]

def sortAphabetical(lists) -> list : 
    lists.sort(); return lists

# print(sortAphabetical(thislist))

def sortDescending(lists) -> list :
    lists.sort(reverse = True); return lists

# print(sortDescending(thislist))


def myFunc(n) :
    return abs(n - 50)

nums = [20, 30, 10, 60, 90, 200]
def sortCloseTo(nums : list) -> list :
     nums.sort(key=myFunc); return nums

print(sortCloseTo(nums))



#  letters being sorted before lower case letters:


def inCaseSensitive(fruits : list) -> list :
    fruits.sort(key= str.lower); fruits.reverse(); return fruits # additional reverse
    
# print(inCaseSensitive(thislist))

