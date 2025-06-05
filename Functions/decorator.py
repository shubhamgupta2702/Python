'''
burger - function
extra cheese - extra feature

main function > function add
without changing the main function code
'''

def myDecorator(func):
  def wrapper():
    print('Something is happening before the func is called !')
    func()
    print("Something is happening after the function is called !")
  return wrapper

@myDecorator
def say_Hello():
  print("Hello !")

say_Hello()