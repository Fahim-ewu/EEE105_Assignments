numletter = 0
numword = 0
numdigits = 0
text = input("Enter your text :")
for a in text :
    if a >= 'a' and a <= 'z' :
        numletter += 1
    elif a >= '0' and a <= '9' :
        numdigits += 1
    elif a == ' ' :
        numword += 1
print("The numbers of letter in the text is-",numletter)
print("The numbers of words in the text is-",numword+1)
print("The numbers of digits in the text is-",numdigits)