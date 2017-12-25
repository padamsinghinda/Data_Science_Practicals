word = input("Enter a word :")

rev_word = []
for i in range(len(word)):
    rev_word.append(word[-i-1])
    
reverse_word = ''.join(rev_word)

print("Reversed word is : %s " % reverse_word)