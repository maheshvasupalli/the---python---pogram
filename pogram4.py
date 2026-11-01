w=input("enter a word:")
s=set(w)
vowels={"a","e","i","o","u"}
v=s.intersection(vowels)
print(v)