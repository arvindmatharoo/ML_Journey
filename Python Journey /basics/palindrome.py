string = "poop"
length = len(string)
leng = length - 1 
x = 0 
for i in range(0,length):
        if string[leng] == string[i] : 
            x += 1 
        leng = leng - 1
if x == length :
    print("the string is palindrome")
else :
    print("not a palindrome")