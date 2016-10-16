__author__ = 'alina'


def difference_aux(mappings, letter1, letter2):
    return mappings[letter1] - mappings[letter2]


def roman_to_arab(mappings, number_str):
    sum = 0

    for i in range(len(number_str) - 1):
        if difference_aux(mappings, number_str[i], number_str[i + 1]) < 0:
            sum -= mappings[number_str[i]]
        else:
            sum += mappings[number_str[i]]

    sum += mappings[number_str[-1]]
    return sum

s1 = "IXCM"
s2 = "VLD"


def arab_to_roman(n):
    pos = 0
    roman = ""
    while n > 0:
        cif = n % 10
        roman_cif = ""
        if cif % 10 == 9:
            roman_cif = s1[pos] + s1[pos + 1]
        elif cif % 10 == 4:
            roman_cif == s1[pos] + s2[pos]
        else:
            if cif // 5 == 1:
                roman_cif += s2[pos]
            if cif % 5 in [1, 2, 3]:
                roman_cif = roman_cif + (s1[pos] * (cif % 5))
        n //= 10

        pos += 1
        roman = roman_cif + roman
    return roman


if __name__ == '__main__':
    mappings = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    mappings2 = {1: 'I', 5: 'V', 10: 'X', 50:'L', 100: 'C', 500: 'D', 1000: 'M'}

    print('XXVII:', roman_to_arab(mappings, 'XXVII'))
    print('CMXCIX:', roman_to_arab(mappings, 'CMXCIX'))

    print('123', arab_to_roman(123))