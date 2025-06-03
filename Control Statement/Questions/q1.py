"""
1-10
even number 
2,4,6,8,10

1,3,5,7,9

n %2 == 0 --> even
"""

for i in range(1,11):
  if i%2 == 0:
    print("even-",i)
  else:
    print("odd",i)