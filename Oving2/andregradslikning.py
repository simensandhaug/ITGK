from math import sqrt
#b)
def quadratic(a, b, c, two):
    if(two):
        return f"Andregradslikningen {likning} har de to reelle løsningene {(-b + sqrt(b**2 - 4*a*c))/(2*a)} og {(-b - sqrt(b**2 - 4*a*c))/(2*a)}"
    else:
        return f"Andregradslikningen {likning} har en reell dobbeltrot {(-b + sqrt(b**2 - 4*a*c))/(2*a)}"

#a)

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

likning = f"{a}*x^2 +({b})*x +({c})"

sqrtRes = b*b - 4*a*c

if(sqrtRes < 0):
    print("2 imaginære løsninger")
    print
elif(sqrtRes > 0):
    print("2 reelle løsninger")
    print(quadratic(a, b, c, True))
else:
    print("En reell dobbeltrot")
    print(quadratic(a, b, c, False))


