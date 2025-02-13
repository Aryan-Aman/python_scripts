def decorator(func):
    def wrapper(arg1, arg2): #In Python, you cannot use two * arguments in a function definition. The correct way to capture all positional arguments is to use *args, and to capture all keyword arguments, you use **kwargs.
        print("i got these args: ", arg1, arg2)
        func(arg1, arg2)
    return wrapper

@decorator
def greet(fname, lname):
    print (f'hello {fname} {lname}')

greet('aman', 'kumar')

'''above code can be replaced by **kwargs also -> arg1, arg2>**kwargs'''
def decorator(func):
    def wrapper(**kwargs): # can't use two * arguments in a function definition.positional arguments  *args, keyword arguments **kwargs.
        print("i got these args: ",kwargs) #orrect way to print the keyword arguments is to pass kwargs directly to the print function as kwargs and not as **kwargs
        func(**kwargs)
    return wrapper

@decorator
def greet(fname, lname):
    print (f'Hello {fname} {lname}')

greet(fname='aman', lname='kumar')