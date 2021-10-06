
users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

print("Användare:")
for key in users.keys():
    print(key)

print()

print("Användare och Lösenord: ")
for key in users.keys():
    print(f"{key}) {users[key]}")

print()

data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

print("Användare och dess Data: ")
for key in data.keys():
    print(f"{key}) {data[key]}")

print()

ans = input("Slå upp användare: ")
if ans in users.keys():
    print(f"Data lagrad för {ans}: {data[ans]}")
else:
    print(f"Användaren {ans} finns inte")