# Draw the environment diagram at the time the statement with the arrow is being executed:
def fuzzle(a, b):
    return a + b # <------

def buzz(a):
    return fuzz(a, square(a))

buzz(2)