def char_fre(string) :
    frequency = {}
    for char  in string :
        if char in frequency : 
            frequency[char] += 1 
        else :
            frequency[char] = 1 
    return frequency
string = 'hello world'
print(char_fre(string))
