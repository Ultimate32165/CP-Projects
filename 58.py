word = input()
low = 0
up = 0
for i in word:
  if i==i.upper():
    up+=1
  else:
    low+=1
if up>low:
  print(word.upper())
else:
  print(word.lower())