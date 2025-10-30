import os, sys  # F401 (unused imports)

def add_numbers(a,b): # E231 (missing whitespace after comma), N802 (function name should be snake_case)
    result=a+b   # E225 (missing whitespace around operator)
    print("Result is: " ,result )  # E201/E202 (whitespace issues), E231 (extra space)
    return result


def UnusedFunction():  # N802 (function name not snake_case), F401 (unused function)
    temp = 123
    return temp


class badClassName:  # N801 (class name should use CapWords convention)
    def method( self):  # E211/E251 (whitespace issues), N802
        print( "Hello" )  # E201/E202
        return 42

x=  1   # E221 (multiple spaces)
y=2
if x==y:   # E225 (missing whitespace around operator)
  print( "Equal") # INDENT error (E111)
