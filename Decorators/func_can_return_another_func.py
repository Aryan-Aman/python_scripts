def greet(style='formal'): 
    '''Default is "formal" ,If no argument is passed when calling 
    get_greeting(), Python automatically assigns style = "formal" '''

    def formal(name='sir'):
        return f"Hello, {name.upper()} best regards!!"
    def casual(name='buddy'):
        return f"Hi, {name.upper()} whats's up?!!"
    
    return formal if style == 'formal' else casual

say=greet()
print(say) #say is a function object here
print(say('chiefsirr'))
print(greet('notformal')('another Buddy'))
