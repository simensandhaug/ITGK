from math import floor, log10
# a)
print("a)\n")
def round_number(n, d):
    return floor((n*10 ** d) + 0.5) / 10 ** d

n_a = float(input("Gi inn et desimaltall: "))
d_a = int(input("Antall desimaler i avrunding: "))
r_a = round_number(n_a, d_a)
res_a = int(r_a) if r_a % 1 == 0 else r_a
d_text = "desimal" if d_a == 1 else "desimaler"
print(f"Avrundet til {d_a} {d_text}: {res_a}")

print("\n")

# b)
print("b)\n")
def combine(x, y):
    if y == 0: return x
    return x + y * 10**-(floor(log10(y))+1)

n1_b = int(input("Oppgi heltallsdelen av tallet (det foran punktum): "))
n2_b = int(input("Oppgi desimaldelen av tallet (det bak punktum): "))
d_b = int(input("Oppgi ønsket antall desimaler i avrunding: "))
r_b = round_number(combine(n1_b, n2_b), d_b) if n2_b // 10 >= 1 else round(combine(n1_b, n2_b))
res_b = int(r_b) if r_b % 1 == 0 else r_b
d_text = "desimal" if d_b == 1 else "desimaler"
print(f"{n1_b}.{n2_b} Avrundet til {d_b} {d_text} blir: {res_b}")

print("\n")

# c)
print("c)\n")

name = input("Jeg heter: ")
arr = name.split(' ')
print(f"The name is {arr[-1]}, {' '.join(arr)}")