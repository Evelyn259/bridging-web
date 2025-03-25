motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)


motorcycles=[]
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'Ford')
print(motorcycles)

del motorcycles[0]

print('after deleting')
print(motorcycles)

popped_motorcycle= motorcycles.pop()
print(f"remaining motorcycles after pop call {motorcycles}")
print(f"popped motorcycle : {popped_motorcycle}")
print(motorcycles)
print(f"popped element {motorcycles.pop(0)}")
print(f"remaining element {motorcycles}")

