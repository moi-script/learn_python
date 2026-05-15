
# multiline string

mult = """
fist line
second line
third line
"""



# slicing
b = "Hello, World!" # start index 2 from 0 stop at before index 5  [start : stop]
part = b[2:5] # 5 - 2 = 3 llo
# print(b[2:5])
# slice from the start
fistChar = b[:5] # all character before index 5 --> hello
# slice to the end
atEnd = b[2:] # llo, World!



# negative index 


"""
 W  o  r  l  d  !
 7  8  9 10 11 12
-6 -5 -4 -3 -2 -1

"""

negAt = b[-5:-2]  # o -> before -2 which is l = orl

  
  
  

# modifying string methods 

#upper -> upper case
#lower -> lower case
#strip - remove white space from beginning and  end
#replace -> change char
#split -> return array base on arg


# task 1

text = "PythonProgramming"

def fistChar(text, end) :
    return  text[:end]

def lastChar(text, start) :
    return text[start:]
# print(fistChar(text, 6))
# print(lastChar(text, 6))

def sliceChar(text, value) :
    toSlice = text.find(value)
    return text[toSlice : toSlice + len(value)]

def sliceCharV2(text, start, end) :
    return text[start : end]

# print(sliceCharV2(text, 2, 5))





text = "LearnPythonFast"

learn = text[:len("Learn")]
pyth = text[text.find("Python") : text.find("Python") + len("Python")]
Fast = text[text.find("Fast"):]
reverseStr = text[::-1]
# learn, pyth, Fast = Fast, pyth, learn

print(reverseStr)




