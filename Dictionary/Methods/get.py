profile = {
  'name':'raju','age':25,'salary':78000
}

# profile.get()
age2 = profile.get('age2') #not found
age = profile.get('age', 'Not Found') #default value
print(age)  
print(age2) # not found