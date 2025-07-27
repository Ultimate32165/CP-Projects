a= input()
low=0
up=0
for i in a:
    if i==i.lower():
        low+=1
    elif i==i.upper():
        up+=1
    
if up>low:
    print(a.upper())
elif low>up:
    print(a.lower())
else:
    print(a.lower())