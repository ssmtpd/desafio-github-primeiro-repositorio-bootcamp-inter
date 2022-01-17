motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
lastOwned = motorcycles.pop()
firstOwned = motorcycles.pop(0)
print(motorcycles)
print("The first motorcycle I owned was a " + firstOwned.title() + ".")
print("The last motorcycle I owned was a " + lastOwned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
tooExpensive = 'ducati'
motorcycles.remove(tooExpensive)
print(motorcycles)
print("The " + tooExpensive.title() + " is too expensive for me.")