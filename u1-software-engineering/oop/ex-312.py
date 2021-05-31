# Draw a picture of the relevant binding environments when the statement with the arrow is being executed. What value does the procedure return?
def f(a):
    return a + g(a)

def g(b):
    return a + b # <--------

f(3)