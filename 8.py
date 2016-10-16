import operator
import functools

__author__ = 'alina'


def print_permutations(s, inf, sup):
    if inf == sup:
        yield "".join(s)

    for i in range(inf, sup):
        s[inf], s[i] = s[i], s[inf]
        yield from print_permutations(s, inf + 1, sup)
        s[inf], s[i] = s[i], s[inf]


def print_permutations_lexicographic(s, inf, sup):
    if inf == sup:
        print("".join(s))

    for i in range(inf, sup):
        s[inf:sup] = sorted(s[inf:sup])
        s[inf], s[i] = s[i], s[inf]
        print_permutations_lexicographic(s, inf + 1, sup)
        s[inf], s[i] = s[i], s[inf]


def print_permutations_with_sol(s, sol, sol_indices):
    if len(sol) == len(s):
        print("".join([str(x) for x in sol]))

    for i in range(0, len(s)):
        if i not in sol_indices:
            sol.append(s[i])
            sol_indices.add(i)
            print_permutations_with_sol(s, sol, sol_indices)
            sol.remove(s[i])
            sol_indices.remove(i)


def print_all_subsets(s):
    for i in range(0, 2**len(s)):
        p = 0
        print("[ ", end="")
        while i > 0:
            if i & 1 == 1:
                print(s[p], end=" ")
            p += 1
            i >>= 1
        print("]")


def print_all_subsets_2(arr, pos, sol):
    print("".join([str(x) for x in sol]))

    for i in range(pos, len(arr)):
        sol.append(arr[i])
        print_all_subsets_2(arr, i + 1, sol)
        sol.remove(arr[i])


def print_subsets_sum_s(arr, s, pos, sol):
    if functools.reduce(operator.add, sol, 0) == s:
        print(" ".join([str(x) for x in sol]))

    for i in range(pos, len(arr)):
        sol.append(arr[i])
        print_subsets_sum_s(arr, s, i + 1, sol)
        sol.remove(arr[i])


def print_all_combinations(arr, k, pos, sol):
    if len(sol) == k:
        print("".join(sol))
        return

    for i in range(pos, len(arr)):
        sol.append(arr[i])
        print_all_combinations(arr, k, i + 1, sol)
        sol.remove(arr[i])


def print_all_arrangements(arr, k, sol, sol_indices):
    if len(sol) == k:
        print("".join(sol))
        return

    for i in range(0, len(arr)):
        if i not in sol_indices:
            sol.append(arr[i])
            sol_indices.add(i)
            print_all_arrangements(arr, k, sol, sol_indices)
            sol.remove(arr[i])
            sol_indices.remove(i)


def print_crossproduct_nokia(number, mappings, k, sol):
    if k == len(number):
        print("".join(sol))
        return

    for ch in mappings[int(number[k])]:
        sol.append(ch)
        print_crossproduct_nokia(number, mappings, k + 1, sol)
        sol.remove(ch)


def print_crossproduct_sets(sets, k, sol):
    if len(sol) == len(sets):
        print("".join([str(x) for x in sol]))
        return

    for a in sets[k]:
        sol.append(a)
        print_crossproduct_sets(sets, k + 1, sol)
        sol.remove(a)


def print_sol(n, sol):
    for i in range(n):
        for j in range(n):
            if (i, j) in sol:
                print('R', end='')
            else:
                print('*', end='')
        print()

def check_diag(l, c, sol):
    for a,b in sol:
        if abs(a - l) == abs(b - c):
            return False
    return True


def queens(n, lin, sol_lines, sol_cols, sol):
        if len(sol) == n:
            print_sol(n, sol)
            print()

        for i in range(n):
            if lin not in sol_lines and i not in sol_cols and check_diag(lin, i, sol):
                sol.append((lin, i))
                sol_lines.add(lin)
                sol_cols.add(i)
                queens(n, lin + 1, sol_lines, sol_cols, sol)
                sol.remove((lin, i))
                sol_lines.remove(lin)
                sol_cols.remove(i)

if __name__ == '__main__':
    s = ['c', 'a', 'b']
    #for p in print_permutations(s, 0, len(s)):
    #    print(p)

    s1 = ['f', 'a', 'z', 'r', 'e']
    #print_permutations_lexicographic(s1, 0, len(s1))

    s2 = [1, 2, 3]
    #sol_indices = set()
    #print_permutations_with_sol(s2, [], sol_indices)

    # print_all_subsets(s2)
    #print_all_subsets_2(s2, 0, [])

    mappings = {1: '.', 2: 'abc', 3: 'def',
                4: 'ghi', 5: 'jkl', 6: 'mno',
                7: 'pqrs', 8:'tuv', 9:'wxyz',
                0: ' '}

    #print_crossproduct_nokia('823', mappings, 0, [])


    #print_all_combinations('abcd', 2, 0, [])
    #sol_indices = set()
    #print_all_arrangements('abcd', 2, [], sol_indices)

    s3 = [1, 5, 4, 2]
    #print_subsets_sum_s(s3, 6, 0, [])

    #print_crossproduct_sets([['a', 'b'], [1, 2], ['x', 'y']], 0, [])

    sol_lines = set()
    sol_cols = set()
    queens(4, 0, sol_lines, sol_cols, [])