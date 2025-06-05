# check pass length

def checkPassword(password):
  if len(password) < 8:
    raise Exception("Error: Password must be >=8 characters")
  print("Password is Strong")
  
try:
  password = input('Enter a password: ')
  checkPassword(password)
except Exception as e:
  print(e)