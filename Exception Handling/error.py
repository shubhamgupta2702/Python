try:
  num = int(input('enter a number: '))
  result = 10 / num
  print(f'result is - {result}')
  
except ZeroDivisionError:
  print("You cannot divide with zero")
  
except ValueError:
  print('You cannot divide with string')