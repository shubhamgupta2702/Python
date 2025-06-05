'''
opening a file
open('file_name','mode')
'''

file = open('C:\\Users\\shubh\\OneDrive\\Desktop\\python\\File Handling\\files.txt', 'r')

content = file.read()
print(content)

file.close() 