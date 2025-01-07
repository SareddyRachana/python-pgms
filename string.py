s=input()
l=[]
for i in s.split():
    l.append(i[::-1])
s1=' '.join(l)
print(s1)