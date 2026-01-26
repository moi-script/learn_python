import string


# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()



# generate an alpabet

alphabet_list = list(string.ascii_lowercase)

new = alphabet_list.append([10, 20, 30]) #  this new  does not get the latest value after append

# alphabet_list.clear()

newList = alphabet_list.copy()

# print(newList.count("a"))

# print(alphabet_list)
newList.extend([10, 20, 30])


# index(elmnt, start, end)
# try : 
#     print(newList.index(10, 4, 26))

#     print('hello')
# except ValueError :
#     print("There is no 10 in the list from range 4 -> 26")
# finally :
#     print("done")


# insert(pos, element)
newList.insert(10, "hello world")

print(newList)


# pop(pos)

newList.pop(0)

print(newList)


# remove(element)


newList.remove('b')
print(newList)




# sort(key=fn, reverse=True or false) 
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]



def getYears(car) : 
    return car['year']

cars.sort(key=getYears)
print(cars)

# how key was process in sorted
# decorated = [(key(item), item) for item in cars]
# decorated.sort()
# cars[:] = [item for (_, item) in decorated] # cars[:] -> all entire list, 0 -> max length with 1 step






