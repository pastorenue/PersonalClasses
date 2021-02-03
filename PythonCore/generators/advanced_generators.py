import is_palindrome

def infinite_palindrome():
    num = 0
    while True:
        if  is_palindrome.is_palindrome(num):
            i = (yield num) # Note that this is no longer a statement. This was modified as of Python 2.5 to be an expression
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindrome()

for i in pal_gen:
    digits = len(str(i))
    print(i)
    if digits == 5:
        pal_gen.throw(ValueError("Digit too large")) # throws an exception
        # pal_gen.close() # Or close the generator
    pal_gen.send(10 ** (digits))
