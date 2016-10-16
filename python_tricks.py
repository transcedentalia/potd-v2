class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Number(self.num + other.num)

    def __str__(self):
        return str(self.num)

class Triple:
    '''
    Multiply by three.
    '''
    def __call__(self, *args, **kargs):
        return 3 * args[0]

def dividedByThree(n):
    for i in range(n):
        if i % 3 == 0:
            yield i

if __name__ == '__main__':
    '''n = Number(5)
    m = Number(6)

    print(n - m)'''

    # print((1).__add__(2))

    t = Triple()
    print(t.__doc__)

    gen = dividedByThree(10)
    print(list(gen))
    for j in gen:
        print(j, end=" ")

    for j in gen:
        print(j, end="#")
