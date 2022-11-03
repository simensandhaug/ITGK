from random import randint

max_rand_int = int(input("Max random integer: "))
target = int(input("Target: "))

generated = randint(0, max_rand_int)
print(generated)

while generated != target:
    generated = randint(0, max_rand_int)
    print(generated)
