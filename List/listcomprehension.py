'''
[expression for item in iterable if condition]

e - x * 2
item - 
iterable - range(1,10)
condition - optional


square = []
for i in range(1,11):
  square.append(i**2)
print(square)
'''

# squares = [i **2 for i in range(1,11)]
# print(squares)

squares = [i **2 for i in range(1,11) if i%2 == 0]
print(squares)
