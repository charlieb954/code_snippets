# DECORATOR
# function must be called in the decorator else it won't execute
from time import time

def timer_decorator(func):
    def inner(*args):
        start = time()
        func(*args)
        end = time()
        return f"Function took {end-start} seconds to execute"
    return inner # inner must be returned else error

@timer_decorator
def print_world():
    print("hello world")
    
print(print_world())