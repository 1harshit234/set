set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

y = set1.intersection(set2)
z = set2 - y 
q = set1 - y
q.update(z)
print(q)
