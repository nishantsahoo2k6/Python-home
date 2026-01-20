word=["apple","banana","pineapple"]
def longest_word(word):
    max = word[0]
    for i in word:
        if len(i)>len(max):
            max = i
    return max
print(longest_word(word))
