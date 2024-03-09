num = {1,2,3,4,5}
num2 = set([4,5,6,7])
'''
print(num)
num2.add(7)
num2.remove(7)
print(num2)
print(7 in num2)

'''

print(num | num2)
print(num & num2)
print(num - num2)