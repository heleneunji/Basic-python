a='a:b:c:d'
print(a.replace(':',"#"))

b=a.split(':')
c='#'.join(b)
print(c)

d=[1,3,5,4,2]
d.sort()
d.reverse()
print(d)

e=[1,2,3,4,5]
e.remove(4)
e.remove(5)
print(e)

f=[1,2,3,4,5]
f[3:]=[]
print(f)

g=['Life','is','too','short']
h=' '.join(g)
print(h)

print(type(g))
print(type(h))

i=['a','a','b','c','a']
print(i.count('a'))