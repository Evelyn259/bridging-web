"""4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)"""
million= list(range(1,1001))
print(million)
for number in million:
    print(number, end=" ")