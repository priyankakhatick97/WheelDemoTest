import sys
sys.path.append('/Workspace/Users/priyanka.khatick@tigeranalytics.com/DemoTest')

from Test1 import *

def func_test():
    print("Welcome to the test.py file")

def print_name(name):
    print(f"Hello my name is test {name}")

def print_test_age(age):
    print_age(age)

func_test()
print_age(25)
print_test_age(30)
print_name("Priyanka")
function_init()