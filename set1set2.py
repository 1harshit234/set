set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
y = set1.intersection(set2)
if y == {}:
    print("nonex")
else:
    print("two sets have some common elemnet in it",y)
    