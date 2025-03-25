locations =['Korea','Japan','Paris', 'London','China']
print(locations)

print(f"order the locations: {sorted(locations)} ")
#print (sorted(locations))
print(f"original locations: {locations} ")
#print(locations)

locations.reverse()
print(f"reverse order of list {locations}")


locations.sort() #accending order
print(f"after sorting in alphabet order {locations}")

locations.sort(reverse=True)
print(f"after sorting with decresing order {locations}")

print(f"number of places that i like to travel {len(locations)}")

#py
# print(locations[-6])
