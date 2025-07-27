word = input()
reversed_word = word[::-1]
word2 = input()
if word2.lower() == reversed_word.lower():
    print("YES")
else:
    print("NO")
