''' Write a function that takes an input string and returns a compressed 
form of the string. The compressed form should represent consecutive 
characters by indicating their count. For example, the input string 
'aaabbc' should be converted to 'a3b2c1'. '''

s = 'aaaabbbccaa'
i = 0
j = 1
outputt = ''

while i < len(s) - 1:
    if s[i] == s[i+1]:
        j += 1
    else:
        outputt += str(s[i]) + str(j)
        j = 1
    i += 1

outputt += str(s[i]) + str(j) 

print(outputt)