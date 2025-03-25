friends=['Robert','Carl','Petra']
print("WoW! we've got a bigger dinner table.")
friends.insert(0,'Evelyn')
friends.insert(2,'Rezzy')
friends.insert(4,'Han')
friends.insert(5,'Cody')
print(f"{friends[0]}, please join the dinner tonight.")
print(f"{friends[1]}, please join the dinner tonight.")
print(f"{friends[2]}, please join the dinner tonight.")
print(f"{friends[3]}, please join the dinner tonight.")
print(f"{friends[4]}, please join the dinner tonight.")
print(f"{friends[5]}, please join the dinner tonight.")
print(f"{friends[6]}, please join the dinner tonight.")

print("Unlucklily, there are only two people we can invite for dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")

print(f"{friends[0]}, You are still invited.")
print(f"{friends[1]}, You are still invited.")

del friends[0]
del friends[0]

print(f"after deleting two guests from list {friends}")