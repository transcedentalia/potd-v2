__author__ = 'alina'


def pairs_sum_s(arr, s):
    elems = dict()

    for i, a in enumerate(arr):
        if a not in elems:
            elems[a] = [i]
        else:
            t = elems[a]
            t.append(i)
            elems[a] = t

    for i, a in enumerate(arr):
        tmp = s - a
        if tmp in elems:
            for t in elems[tmp]:
                if t > i:
                    print('(', a, ',', tmp, ')')


def triple_sum_s(arr, s):
    elems = dict()

    for i, a in enumerate(arr):
        if a not in elems:
            elems[a] = [i]
        else:
            t = elems[a]
            t.append(i)
            elems[a] = t

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tmp = s - arr[i] - arr[j]
            if tmp in elems:
                for t in elems[tmp]:
                    if t > i and t > j:
                        print('(', arr[i], ',', arr[j], ',', tmp, ')')


if __name__ == '__main__':
    my_arr1 = [3, 4, 5, 4, 2, 7, 1]
    pairs_sum_s(my_arr1, 7)
    triple_sum_s(my_arr1, 8)
