def greet(name='chief'):
    
    def casual_greet(name='buddy'):
        return f"Hi, {name.upper()} whats's up?!!"
    def formal_greet(name='sir'):
        return f"Hello, {name.upper()} best regards!!"
    
    if name=='chief':
        return formal_greet
    else:
        return casual_greet

say=greet()
print(say) #say is a function object here
print(say('chief Aman'))
print(greet('casual_greet')('another Buddy'))