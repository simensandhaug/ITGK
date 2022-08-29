# a)
print("a)\n")

stoff = input("Si et stoff du er i besittelse av: ")
molvekt = float(input("Hva er molvekt i gram for vann? "))
gram = float(input("Hvor mange gram vann har du? "))
mol = gram / molvekt
AVOGADRO = 6.022e23
molekyler = mol * AVOGADRO
print(f"Du har {format(molekyler, '.1e')} molekyler {stoff}")

print ("\n")

# b)
print("b)\n")

POSSIBLE_MELODIES = 8.25e19

user_heard = int(input("Antall ulike 10-toners melodilinjer du har hørt? "))

print(f"Du har hørt {format(user_heard / POSSIBLE_MELODIES * 100, '.1e')} prosent av melodier som er mulig.")