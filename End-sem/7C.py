word = input("Enter a word: ")
def vowels(word):
    c=0
    for i in word:
        if i in "aeiouAEIOU":
            c+=1
    return c

print(vowels(word))