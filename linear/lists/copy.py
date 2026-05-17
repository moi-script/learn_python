thislist = ["apple", "banana", "cherry"]

newList = thislist.copy()
# print(newList == thislist) # true

anotherNewList = list(newList)
# print(anotherNewList == thislist) # true

sliceCopyTricks = thislist[:]
# print(sliceCopyTricks == thislist)  # true


