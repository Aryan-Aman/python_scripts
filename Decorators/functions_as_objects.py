#defined a function
def greet(name='aman'):
    return f"Hello, {name.upper()} !!"
print(greet())

say=greet #assigning the function to a variable so no paranthesis

print(say('siemens'))

del greet

try:
    # print(greet('without delete'))
    print(greet())
except NameError as e:
    print(e)

print (say('still works even after deleting greet')) 
