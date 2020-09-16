from time import sleep

# SIMPLE GENERATOR USECASE
def generator():
    for i in range(5):
        sleep(0)
        yield i

for i in generator():
    print(i)
    print(f"could perform futher actions on {i}")

# SIMPLE CHUNKER SYNTAX
def chunker(ls, n):
    '''
    Used to chunk large lists into smaller objects ready for further work
    
    Parameters
    ==========
    ls = list: to be chunked
    n = int: number of chunks per return
    
    Returns
    =======
    the next n items from the the supplied ls
    '''
    for i in range(0, len(ls), n):
        yield ls[i:i+n]

my_list = list(range(0,15))
for i in chunker(my_list, 3):
    print(i)