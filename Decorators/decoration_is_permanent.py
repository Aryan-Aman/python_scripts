def uppercase_decorator(func):
    def wrapper(name):
        return func(name).upper()
    wrapper.__wrapped__ = func # __wrapped__ is a special attribute that is used to store a reference to the original function when a function is wrapped by a decorator.
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: "HELLO, ALICE!"

# Now __wrapped__ exists, and we can "undo" the decorator
greet = greet.__wrapped__
print(greet("Alice"))  # Output: "Hello, Alice!"


#importing functools then use __wrapped__ attribute can also be done