# we can use this as default
import modules

# but we can name here
import modules as tests
# tests.test()

# also importing a single object specifically

from modules import test # test is the function name modules.py

test()


# built in modules 
#   platform 

import platform

systemName = platform.system()

dirs = dir(platform)
# print(systemName)


for i in range(len(dirs)) :
    print(dirs[i])


    