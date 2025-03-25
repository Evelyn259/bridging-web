my_pizzas = ['California pizza','Cheese pizza','Hawaiian pizza','Greek Pizza']
friend_pizzas=my_pizzas[:]

my_pizzas.append('hawaii pizza')
friend_pizzas.append('vegetable pizza')

print("My favourite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)
    
print("My friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)    