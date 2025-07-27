s = input()[1:-1].strip()
print(0 if not s else len(set(i.strip() for i in s.split(","))))
