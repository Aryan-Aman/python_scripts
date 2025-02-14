'''Stack memory > References Methods Call-()
   Private heap memory > Objects and data'''
'''x referring to object 5 > stack mmry // 5 is stored in heap mmry'''
x=5 
print(type(x)) #<class 'int'>
print(id(x))   #140729867966352

y=x
print(type(y)) #<class 'int'>
print(id(y))   #140729867966352

'''x & y refer same object 5'''

x=x+1          
print(type(x)) #<class 'int'> 
print(id(x))   #140729867966384 x is now referring to new object 6

z=5
print(id(z))   #140729867966352 z is referring to same object 5
print(type(z))

'''when one objct in heap mmry one or more variable can refer that object
x->6 , y,z->5'''



#MEMORY ALLOCATION IN PYTHON
 def func2(z):
    q=z+1
    return q


def func1(x):
    z=x+10
    p=func2(z)
    return p

#main
x=5
y=func1(x)
print(y)
'''1.)x stored in stack & refer 5 which is in heap
 2)AWK func also stores in stack so,> func1 block in stack 
 3) now z in func1 block stack mmry & refer 15
 4) p in func1 block of stack mmry 
 5)func2 block in stack mmry> now q in func2 block of stack mmry & refer 16
 6) return q=16 > p=16 so refer 16
 7) func1 return p> so y also refer 16
 8) extra variable left in garbage collector
 9)in end check in heap mmry objcts which are not reffered by any variable-treats as dead object k/as Reference counting'''
