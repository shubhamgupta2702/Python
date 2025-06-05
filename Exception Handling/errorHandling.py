try:
  file = open('C:\\Users\\shubh\\OneDrive\\Desktop\\python\\Exception Handling\\errors.txt', 'r')
  content = file.read()
  print(content)
  
except FileNotFoundError:
  print('File not found')
  
finally:
  file.close()
  print("File operation successfull")