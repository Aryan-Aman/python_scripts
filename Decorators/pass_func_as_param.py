def scream():
    return 'Roar!!'

def dosomething(Func):
    print('I scream before i do something')
    print(Func()) 
    print('I scream after i do something')

dosomething(scream) 
