# Write a program to accept the string s from the user and print all alphabets in one line separated by , before

# first occurrence of vowels .

s="program"
vowel="aeiouAEIOU"
res=""

for i in s:
    if i in vowel:
        continue
    else:
        res+=i+","
print(res)


