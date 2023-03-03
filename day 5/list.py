lst=list()

fruits=['banana','orange','mango','coconut','apple']
print('Number of fruits:', len(fruits))
fruits.index('0')
fruits.index(2)
fruits.index(4)

mixed_data_types=['Jose Luis','17','1,75','soltero','C/Salvador Sanchez Barbudo']
print(mixed_data_types)

it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

number_of_companies=7
print('number_of_companies')

print('0', '1', '6')

it_companies.append('Netflix')
print(it_companies)

mayuscula= it_companies[2]
print(mayuscula.upper)

join1= '#'.join(it_companies)
print(join1)

does_exist = 'Google' in it_companies
print(does_exist) # True

it_companies.sort()
print(it_companies)

it_companies.reverse=['Amazon', 'Oracle', 'IBM', 'Apple', 'Microsoft','Google', 'Facebook']
print(it_companies.reverse)

threfirt=it_companies[0:3]
print(threfirt)

lastthree=it_companies[4:7]
print(lastthree)

inthemiddle=it_companies['Apple']
print(inthemiddle)

it_companies.remove('Facebook')

it_companies.remove[1:5]

it_companies.pop(6)

it_companies.remove[0:6]

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print(front_end)
back_end = ['Node','Express', 'MongoDB']
print(back_end)

full_stack=front_end + back_end
print(full_stack)
