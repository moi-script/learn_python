# sets are unordered, unchangeable, unindexed

import string

testSet = set(string.ascii_uppercase)

print(testSet)



# True and 1 is the same value in sets also False and 0 



# cannot modify items in set, but can add items


lowerAlphabet = set(string.ascii_lowercase) # will become randomized order 

testSet.add("newvalue".upper())
testSet.update(lowerAlphabet) # also we can do this using list, dictionary, tuples etc

# print(testSet)

