def nani(func):
    def wrapper(*args, **kwargs):
        z=[]
        for i in args:
            if i is None:
                z.append(0)
            else:
                z.append(i)
        return func(*z, **kwargs)
    return wrapper


def a(x, y):
    sum = x + y
    return sum

def b(x, y):
    notsum = x - y
    return notsum

def v(x, y):
    um = x * y
    return um

def g(x,y):
    delen=x//y
    return delen

@nani
def main(x, y):
    sum1 = a(x, y)
    notsum1 = b(x, y)
    um1 = v(x, y)
    delen1=g(x,y)
    return sum1, notsum1, um1, delen1


print(main(None, 2))
