import functools

__author__ = 'alina'

def countOneBits(n):
    count = 0

    while n > 0:
        count += n & 1
        n >>= 1

    return count

def positionOneBit(n):

    step = 1
    pos = -1

    while n > 0:
        x = n & 1
        if x == 1:
            if pos != -1:
                return -1
            else:
                pos = step

        n >>= 1
        step += 1

    return pos


def detect_missing(arr, n):
    sum1 = sum2 = 0
    for a in arr:
        sum1 ^= a

    for a in range(1, n + 1):
        sum2 ^= a

    print(sum1 ^ sum2)


def xor(a, b):
    return a ^ b


def detect_missing_2(arr, n):
    return functools.reduce(lambda a, b: a ^ b, arr, 0) ^ functools.reduce(xor, range(1, n + 1), 0)


if __name__ == "__main__":
    #n = int(input())

    #for i in range(n):
    #    print(countOneBits(int(input())))

    #for i in range(n):
     #   print(positionOneBit(int(input())))

    detect_missing([1, 5, 3, 4, 2, 7], 7)
    print(detect_missing_2([1, 5, 3, 4, 2, 7], 7))
