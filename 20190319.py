a=(1,2,3)
b=(4,)
print(a+b)

c={'name':'홍길동','birth':'1128','age':'30'}
print(c)

c['id']=1912345
print(c)

print(c.get('major','unkwon'))

d=[1,1,1,2,2,3,3,3,4,4,5]
e=set(d)
print(e)

List=[1,2,3]
Set=set([1,2,3])
List.append(3)
Set.add(3)
print(List)
print(Set)

a=[1,2,3]
b=[1,2,3]
print(a is b)