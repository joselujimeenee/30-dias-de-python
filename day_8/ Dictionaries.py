empty_dict=('dog')
print('empty_dict')

dog={
'name_dog': 'Thunder' ,
'colour_dog': 'Brown' ,
'bredd_dog' : 'German shepherd' ,
'legs_dog' : '4' ,
'age_dog': '8'
}
print('name_dog')
print('colour_dog')
print('bredd_dog')
print('legs_dog')
print('age_dog')

empty_dict('student')
print('empty_dict')
student={
'first_name':'José Luis' ,
'last_name': 'Jiménez' , 
'gender': 'Masculino' ,
'age': '17' ,
'marital_status': 'Soltero' ,
'skills':['deportista' , 'empatico' , 'listo' , 'sociable'] ,
'country': 'España' , 
'city': 'Jerez de la Frontera' ,
'address':{
'street': 'C/Salvador Sanchez Barbudo' ,
'zipcode': '11405' , 
}
}
print('first_name')
print('last_name')
print('gender')
print('age')
print('marital_status')
print('skills')
print('country')
print('city')
print('address')

print(len(student))

values=student.values('skills')
print(values) 
student={'skills': 'values'}
print('skills' in student)

student['skills'] = 'gracioso' , 'habil'
print=student

keys=student.keys()
print(keys)

values=student.values()
print(values)

student= {}
print(student.items(student))
