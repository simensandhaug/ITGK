tall = int(input("Input number: "))


def absoluttverdi(x):
    if x < 0:
        return -x
    return x


print(f"Absoluttverdi av {tall} = {absoluttverdi(tall)}")
