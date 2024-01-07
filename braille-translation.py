def get_braille_string(index, _braille_strings):   
    if _braille_strings[index] != None: # if letter string is already in array
        return _braille_strings[index]
    braille_string = ''
    if index == 3 or index == 4: # if letter is not already in array and letter is 'd' or 'e' 
        similar_string = _braille_strings[8 - 2*index] # strings are similar because the only difference is a bump on dot 5. 'd' is similar to 'c'; 'e' is similar to 'a'.
        braille_string = similar_string[:4] + '1' + similar_string[5] # braille translation of letter  
    if index > 4 and index < 8:
        similar_string = get_braille_string(index-3, _braille_strings) # strings are similar because the only difference is a bump on dot 2
        braille_string = similar_string[0] + '1' + similar_string[2:] 
    if index == 8 or index == 9:
        similar_string = get_braille_string(index-3, _braille_strings) # strings are similar because the only difference is that dot 1 is flat
        braille_string = '0' + similar_string[1:]
    if index > 9 and index < 22: 
        similar_string = get_braille_string(index-10, _braille_strings) 
        if index < 20:
            braille_string = similar_string[:2] + '1' + similar_string[3:]
        else:
            braille_string = similar_string[:5] + '1'
    if index >= 23:
        similar_string = get_braille_string(index-11, _braille_strings)
        braille_string = similar_string[:5] + '1'
    _braille_strings[index] = braille_string # updates array to include translation
    return braille_string
s = input("Enter s: ")
output = ''
braille_strings = [None] * 26 # array will hold braille strings for each letter
braille_strings[0] = '100000' # represents 'a' in braille
braille_strings[1] = '110000'
braille_strings[2] = '100100'
braille_strings[22] = '010111' # represents 'w', which is an exception to braille 
for char in s:
    if (char == ' '):
        output += '000000' # space in braille
    else:
        letter_index = ord(char.lower()) - 97 # maps letter to index in array
        if char.isupper():
            output += '000001' 
        output += get_braille_string(letter_index, braille_strings)
        print(braille_strings)
print(output)