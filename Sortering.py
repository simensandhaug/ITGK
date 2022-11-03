liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]

def bubble_sort(l):
    sorted = False
    i = 0
    while not sorted:
        if(i + 1 > len(l) - 1):
            sorted = True
        print(i + 1, len(l))
        if(l[i] > l[i + 1]):
            tmp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = tmp
            i=0
        i += 1
    return l
            

print(bubble_sort(liste))
# Output blir:
# [1, 2, 3, 6, 6, 7, 9, 21, 23, 33, 34, 34, 36, 45, 45, 56, 65, 78]