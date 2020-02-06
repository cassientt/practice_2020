def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Adam', 45, gender='M', job='Engineer'))