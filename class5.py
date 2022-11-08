person = {
    'firstName':"chinmay",
    'lastName':'deshpande',
    'age':12,
    'skills':["python","java","javascript"]
}

# retrive
print(person['firstName'])
print(person['lastName'])
print(person['age'])
print(person['skills'])

#Update

person['firstName'] = 'Shriram'
print(person)
person['lastName']='Bhojne'
person['age']=31
person['skills']='Java'
print(person)

#add
person['city']='Tuljapur'

person['JoB']='CUCUMBER'
print(person)

#Update
person['city']='Latur'
print(person)

person['firstName']='Mayuri'
print(person)