a = [1, 2, 3, "py"]
b = [4, 5, 6, "py"]

# set function
s1 = set(a)
s2 = set(b)

s3 = s1.intersection(s2)
print(s3)
print(list(s3))