__author__ = 'alina'


def check_parantheses(s):
    count = 0
    for ch in s:
        if count < 0:
            return False
        
        if ch == '(':
            count += 1
        else:
            count -= 1

    return count == 0

if __name__ == '__main__':
    print(check_parantheses("(((()"))
    print(check_parantheses("(())()"))