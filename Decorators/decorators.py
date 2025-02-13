'''decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.'''
def decorator(func_to_decorate):
    def wrapper():
        print('execute this before the func_to_decorate')
        func_to_decorate()
        print('execute this after the func_to_decorate')
    return wrapper



# @decorator
def isolated_func():
    print('dont change me')

# isolated_func()

isolated_func_decorated=decorator(isolated_func) #this is same as @decorator
isolated_func_decorated()