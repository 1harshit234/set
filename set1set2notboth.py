set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
"""y = set1.intersection(set2)
print(y)
set1.update(set2)
print(set1)
z = set1 - y
print(z)
"""

####using symmetric difference
#We are calling the symmetric_difference_update() method, which determines the symmetric difference between num1 and num2, which contains the elements that are either in Set num1 or in Set num2 but not both,
set1.symmetric_difference_update(set2)
print(set1)