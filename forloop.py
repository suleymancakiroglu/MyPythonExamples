"""
First loop is 'in'.The ‘in’ operator is used to check if a value exists in a sequence or not. Evaluates to true if it finds a variable in the specified sequence and false otherwise.
"""
a = [1,2,3,4,5,6,7,8]
print(not "r" in a) 
"""
Second loop is 'for'.The 'for' function is used to continous works.
"""
total = 0
students = [1,2,3,4,5,6]

for stu in students:
    total=total+stu
    print(total)

"""
Other loop is in the ‘dictionary’.
"""
dicto = {"ein" : 1,"zwei" : 2,"drei" : 3,"vier" : 4,"fünf" : 5}
for number in dicto:
    print(number)