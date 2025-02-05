import time
from termcolor import *

tests = {'test1' : True, "test2" : False, "test3" : True}

# for i in range(10):
#     cprint('\r{}>'.format('='*i), end='')
#     time.sleep(0.5)

for i in tests:
    if tests[i]:
        cprint(f"{i} : pass", 'green')
    cprint(f"{i} : pass", 'green')