
# new_list = [el for el in my_list if el > my_list[el.numerator-1]]



print({i ** 3 for i in range(5, 10)})
print({i: i * 3 for i in range(10, 20)})

print({i + p for i in range(10, 20) for p in range(100)})
print(range(10))

from random import randint, randrange, random

print(randrange(10, 100, 3))
print(random() * 100)


def gener():
    for i in (10, 20, 30):
        yield i


g = gener()
for el in g:
    print(el)

from functools import reduce


def my_f(el_1, el_2):
    return el_1 + el_2

print(reduce(my_f, [10, 20, 30, 40]))


from itertools import count, cycle

for i in count(6):
    if i > 15:
        break
    else:
        print(i)

z = 0
for i in cycle("GHY"):
    if z > 15:
        break
    else:
        print(i)
        z += 1