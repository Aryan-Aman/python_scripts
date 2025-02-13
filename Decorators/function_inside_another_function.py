def introduce(name='Aman'):
    def say_hi():
        return f"Hi {name.upper()}, This function is called inside introduce function"
    print (say_hi())
introduce()

try:
    print (say_hi())
except Exception as e:
    print (e)
