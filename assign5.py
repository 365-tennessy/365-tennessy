
vehicles = ['bmw','audi','toyota','mercerdes','jeep']

for vehicle in vehicles:
    print(vehicle.title())


#Dictionary is a collection of key value
#syntax: dictionary = ("key"): value
colour= {'colour':'red'}
vehicle= {'type','toyota','plate number','STZ35'}
person={"name":"Val Slim","phone_number":"0745375511","address":"35 ses ame street"}

#accesing values
#print(vehicles["type"])
#print(vehicle["plate_number"])
print(person["name"])
print('{} {}'.format(person['name'], person['address']))

print(type(person["phone_number"]))


#adding values
person["age"]="76"
person["fav colour"]="red"
print(f'{person["name"]} {person["age"]} {person["fav colour"]}')


#looping over dictionaries
for key, value in person.items():
    print(f'("value")("key")')

#Print all colours in uppercase    




