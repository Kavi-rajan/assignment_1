word=input("Enter a word to be reversed :")
rev_word=''
for char in word:
    rev_word = char + rev_word
print("The original word is",word)
print("The reversed word is",rev_word)
