# function which, given some integer x with n digits, removes the digit at index [index]
def remove_digit(x, index, n):
    return (x - (x % 10**(n-index)))/10 + x % 10**(n-1-index)
def solution(L):
    L.sort(reverse = True)
    greatest_num = 0 # greatest number (not necessarily divisible by 3) which can be created from the set digits
    remainder = sum(L) % 3 # equal to the remainder when any number created using all digits in L is divided by three (because of special properties of the number 3)
    min_mod_3 = None # index in L which has the minimum digit, n, in L | n % 3 == remainder == sum(L) % 3
    complements = [None] * 2 # contains indices of minimum numbers a, b | a % 3 == 3 - remainder == a % b. complements[0] <= complements[1]
    for i in range(len(L)):
            if L[i] % 3 == remainder:
                 min_mod_3 = i # minimum value because the digits are iterated over in decreasing order
            if L[i] % 3 == 3 - remainder:
                 complements[1] = complements[0] # these are minimum values because the digits are iterated over in decreasing order
                 complements[0] = i
            greatest_num += L[i] * 10**(len(L)-1-i) # adds based on place of digit (ex: for the digit 933, adds 900, 30, then 3
    if greatest_num % 3 == 0: 
        return greatest_num
    elif min_mod_3 != None: # if there is one digit that can be removed from greatest_num so that the remaining number is divisible by three
        return remove_digit(greatest_num, min_mod_3, len(L))
    elif len(L) > 2: # two digits must be removed from greatest_num so that the remaining number is divisible by three
        result = greatest_num
        for i in range(2):
             result = remove_digit(result, complements[i], len(L)-i)
        return result
    return 0