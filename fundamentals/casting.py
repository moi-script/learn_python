

#int, float, str, list, bool



# explicit -> implicit
#Implicit 
test1 = 10
test2 = 20.25

result= test1 + test2 # auto make the int + float = float



str1 = "3" # no auto since both cannot make the same representation
print(type(int("3"))) # but this will work since "3" can be explicitly convert to number

result2 = test1 + int(str1)
print(result2)


# Explicit -> before operations it manual conversion 



test3 = 300.200

result3 = test1 + int(test3)



# print(int(False))

# print("test 3", result3)

# rule -> if you can convert to other types you can revert it also 

print(type(str(list("abc123"))))