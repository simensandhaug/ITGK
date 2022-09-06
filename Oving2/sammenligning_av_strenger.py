#a)
print("a)\n")

a = input("Matvare 1: ")
b = input("Matvare 2: ")

print(f"Sammenligner {a} og {b}")

if(a.lower() == b.lower()):
    print("Det er samme matvare")
else:
    print("Det er to forskjellige matvarer")

print("\n")

#b)

name1 = input("Navn 1: ")
name2 = input("Navn 2: ")

name_list = [name1, name2]

print("Her kommer sortert liste: ")
print(sorted(name_list))    

