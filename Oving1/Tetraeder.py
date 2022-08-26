# a)
print("a)\n")
def area(a):
    return round(3**(1/2)*(a**2), 3)

h = 3
a = 3*h/(6**(1/2))
print(f"Et tetraeder med høyde {h} har areal {area(a)}")

print("\n")

# b)
print("b)\n")
def volume(a):
    return round(2**(1/2)*(a**3) / 12, 3)

print(f"Et tetraeder med høyde {h} har volum {volume(a)}")

print("\n")

h = int(input("Skriv inn en høyde: "))

a = 3*h/(6**(1/2))

print(f"Et tetraeder med høyde {h} har volum {volume(a)} og areal {area(a)}")



