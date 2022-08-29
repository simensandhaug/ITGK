from prettytable import PrettyTable
table = [['Antall cookies:', 'sukker(g)', 'sjokolade(g)']]

# a)
print("a)\n")
n = int(input("Hvor mange cookies ønsker du å bake? "))
sukker = 400 / 48
smor = 320 / 48
sjokolade = 500 / 48
egg = 2 / 48
hvetemel = 460 / 48
print(f"Antall cookies: {n}\nsukker(g): {sukker * n}\nsmør(g): {smor * n}\nsjokolade(g): {sjokolade * n}\negg: {egg * n}\nhvetemel(g):{hvetemel * n}")
print("\n")

# b)
print("b\n")

n2 = int(input("og hvor mange cookies vil du lage nå? "))
n3 = int(input("og hvor mange cookies vil du lage til slutt? "))

table.append([n, sukker * n, sjokolade * n])
table.append([n2, sukker * n2, sjokolade * n2])
table.append([n3, sukker * n3, sjokolade * n3])

tab = PrettyTable(table[0])
tab.add_rows(table[1:])

print(tab)