import random
from calculator import Calcularot

rand_list = []

for i in range(20):
    rand_list.append(random.randint(0, 100))

calc = Calcularot()

arg1 = random.choice(rand_list)
arg2 = random.choice(rand_list)


print(rand_list)
result = calc.substr(arg1,arg2)

print(f"ARGS: {arg1} and {arg2} . RESAULT:", result)