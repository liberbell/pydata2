animals = ('beer', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'dog': continue
    # if pet == 'velociraptor': break
    print(pet)
else:
    print('that is all the animals')
