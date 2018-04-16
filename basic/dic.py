tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))

print(sorted(tel.keys()))

a = 'guido' in tel
print(a)
b = 'jack' not in tel
print(b)

c = {x: x**2 for x in (2, 4, 6)}
print(c)

group = ['a', 'b', 'c', 'd']
name = ['1', '2', '3', '4']
a = dict(zip(group, name))

print(a)