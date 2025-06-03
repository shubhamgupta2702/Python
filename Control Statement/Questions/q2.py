start = int(input("Enter start number - "))
stop = int(input("Enter stop number - "))

if start < stop:
    skip = int(input("enter no. you want to skip - "))

if skip < start or skip > stop:
    print("Invalid skip number!")

else:
    for i in range(start, stop):
        if i == skip:
            continue
        print(i)
