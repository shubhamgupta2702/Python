num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

choice = input('Enter your choice + - * / % \n')


if choice=="+":
  print("The sum is: ", num1+num2)
  
elif choice=="-" and num1 >= num2:
  print("The diffrence is: ", num1-num2)
  
elif choice=="*":
  print("The multiplication is: ", num1*num2)
  
elif choice=="/":
  print("The division is: ", num1/num2)
  
elif choice=="%":
  print("The remainder is: ", num1%num2)
  
else:
  print("Number 1 is less than number 2")