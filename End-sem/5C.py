word = input("Enter the string")
new_word = ""
for i in word:
    if i in "0123456789":
        continue
    else:
        new_word=new_word+i
print(new_word)
