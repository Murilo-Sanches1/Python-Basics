# int
-269296
269296

# float
27.0
25.688

# string
'c'
'"char"'

# boolean
True
False

# end representa o final do print, por padrão é uma new line end="\n"
print("oba", end=" | ")
print("tudo bem?")

name = "Murilo"
print(name)
print(name.find("i"))

name_input = input("Sobrenome: ")
print(name, name_input)

print(10 / 5)  # divisão retorna um float
print(int(10 / 5))  # casting
print((1 + 2) ** 2)
print(10 / 3)
print(10 // 3)  # floor division
print(10 % 3)  # retorna o resto da divisão

num_input = input("Digite um número: ")
if (type(num_input) == str):
    print(f"Convertendo para inteiro ... pronto! {int(num_input) + 1}")

print("hollow" * 3)

print(5.0 == 5)  # true
print(type(5.0) == type(5))  # false


x = 7
y = 8
z = 0

r1 = x == y  # false
r2 = y > x  # true
r3 = z < x + 2  # true

# or = || and = &&
print(r1 or r2 or r3)
print(False or True or True)
print(not False)
print(not True)
print(not (True or False))
print(False and True)
print(not (False and True))

if 3 == 1:
    print("if")
elif 3 == 2:
    print("elif")
elif 3 == 3:
    print("elif")
else:
    print('else')

numbers = [1, 2, 3]
print(len('abc'))
print(len(numbers))
numbers.extend([4, 5, 6])
numbers.append(7)
print(len(numbers))
print(numbers[0])
print(numbers.pop())
print(numbers.pop(0))
print(numbers[0])

names = ["Murilo", "Sanches"]
namesCopy = names  # usa a mesma referência de memória
namesCopy[0] = "Outro"
print(names, namesCopy)

names2 = ["Murilo", "Sanches"]
namesCopy2 = names[:]  # cria outra memoria para esse objeto
namesCopy2[0] = "Outro"
print(names2, namesCopy2)


# tuple = array immutable
immutable = (1, 2, 3)
# immutable[0] = 2 # TypeError: 'tuple' object does not support item assignment
print(immutable[0])


for i in range(3):
    print(i)

print("=====================")

# range(start, stop, step)
# start = default 0
# stop = required
# step = jump how many
# começa contando do 1, vai parar quando chegar / não der pra chegar no 11
# e incrementa de 3 em 3
for i in range(1, 11, 3):
    print(i, end=" | ")

print()

for x in ['a', 'b', 'c']:
    print(x, end=" | ")

print()

chars = ['x', 'y', 'z']
for x in range(len(chars)):
    print(chars[x], end=" | ")
print()
for x in range(1, len(chars)):
    print(chars[x], end=" | ")

print()

for x, el in enumerate(chars):
    print(x, el)

counter = 0
while True:
    print(counter)
    counter += 1
    if (counter == 5):
        print(counter)
        break

to_slice = [1, 2, 3, 4, 5, 6]
sliced = to_slice[:5]  # igual ao range start : stop : step
print(sliced)
sliced2 = to_slice[1:5]  # igual ao range start : stop : step
print(sliced2)
sliced3 = to_slice[0:6:2]  # igual ao range start : stop : step
print(sliced3)
sliced4 = to_slice[6:0:-2]
print(sliced4)
reverse = to_slice[::-1]
print(reverse)
print("REVERSE"[::-1])

# set - ver se existe ou não - extremamanete rápido para retornar esses booleans
set1 = set()
set2 = {1, 1, 1, 2, 3}
print(set2)  # output - 1, 2, 3
print(type(set1), type({}))
if (1 in set2):
    set2.remove(1)

print(set2)
set2.add(1)
print(set2)

objecT = {"key": 69, 1: "int como key"}
print(objecT["key"])
objecT["key2"] = 96
print(objecT)
print("key" in objecT)
objeT_values = objecT.values()
objeT_values_in_list = list(objecT.values())
print(type(objeT_values))
print(objeT_values)
print(type(objeT_values_in_list))
print(objeT_values_in_list)
print(objecT.keys())

simple_obj = {"apague": 9898989}
for key, val in simple_obj.items():
    print(key, val)
del simple_obj["apague"]
print(simple_obj)

# Comprehensions
print([x for x in range(5)])
print([x for x in range(100) if x % 5 == 0])


def func():
    return 5, 10


func_result1, func_result2 = func()
print(func_result1, func_result2)


def func2(x):
    def func3():
        print(x)
    return func3


print(func2(2))
print(func2(2)())

# unpack = spread *, ** to objects


print([3, 21, 5, 32, 523, 246, 3, 57])
print(*[3, 21, 5, 32, 523, 246, 3, 57])

# throw
# raise TypeError("dkaw")
try:
    x = 5 / 0
except Exception as e:
    print(e)
finally:
    print("finally ocorre dando erro ou dando certo")

# lamb = lambda x: x * 10


def lamb(x): return x * 10


asd = [2, 4, 6, 8, 10]
mp = map(lambda x: x + 2, y)
print(list(mp))
