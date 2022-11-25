str1 = input("Please Enter Your Own Text : ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
punctuaction = 0
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
    
            vowels = vowels + 1

for b in str1:
    if(b == 'b' or b == 'c' or b == 'd' or b == 'f' or b == 'g' or b == 'h' or b == 'j' or b == 'k' or b == 'l' or b == 'm' or b == 'n' or b == 'p' or b == 'q' or b == 'r' or b == 's' or b == 't' or b == 'v' or b == 'x' or b == 'z'):
            consonants = consonants + 1
b = 'B' or b == 'C' or b == 'D' or b == 'F' or b == 'G' or b == 'H' or b == 'J' or b == 'K' or b == 'L' or b == 'M' or b == 'N' or b == 'P' or b == 'Q' or b == 'R' or b == 'S' or b == 'T' or b == 'V' or b == 'X' or b == 'Z'

for l in str1:
    if(l == '0' or l == '1' or l == '2' or l == '3' or l == '4' or l == '5' or l == '6' or l == '7' or l == '8' or l == '9'):
        digits = digits + 1
for a in str1:
    if(a == ' '):
        spaces = spaces + 1
for o in str1:
    if(o == ',' or o == '.' or o == '/' or o == ';' or o == '?' or o == ':' or o == '@' or o == '~' or o == '#' or o == '[' or o == ']' or o == '{' or o == '-' or o == '}' or o == '=' or o == '_' or o == '+' or o == '!' or o == '"' or o == '£' or o == '$' or o == '%' or o == '^' or o == '&' or o == '*' or o == '(' or o == ')'):
        punctuaction = punctuaction + 1
    
    
        f

 
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
print("Total Number of digits in this string  = ",digits)
print("Total Number of spaces in this string  = ",spaces)
print("Total Number of punctuaction in this string = ", punctuaction)