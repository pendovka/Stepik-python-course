''' Write a program that can encrypt and decrypt a substitution cipher. The program takes two input strings of equal length. 
The first string contains characters of the original alphabet, and the second string contains characters of the corresponding 
substituted alphabet. The program then takes a string that needs to be encrypted using the provided key, followed by another 
string that needs to be decrypted.

For example, if the program is given the following input:
abcd
d%#
abacabadaba
#%d%

This means that the character 'a' in the original message is replaced by '' in the cipher, 'b' is replaced by 'd', 'c' is 
replaced by '%', and 'd' is replaced by '#'. The program needs to encrypt the string 'abacabadaba' and decrypt the string '#%d%' 
using this cipher. The resulting strings should be printed as output:

d%d#d
dacabac '''



d = {}
lst1 = []
lst2 = []

initial_message = input()
coded_message = input()
new_initial_message = input()
new_coded_message = input()

for char in initial_message:
    d[char] = coded_message[initial_message.index(char)]
    
for char in new_initial_message:
    for key, value in d.items():
        if char == key:
            lst1.append(value)
    print(*lst1, end = '')
    lst1 = []
print()
for char in new_coded_message:
    for key, value in d.items():
        if char == value:
            lst2.append(key)
    print(*lst2, end ='')

    lst2 = []

    