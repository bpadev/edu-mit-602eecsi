# Draw the environment diagram at the time the statement with the arrow is being executed. 
def fizz(x, y):
    p = x + y
    q = p*p
    return q + x # <----------

fizz(2, 3)