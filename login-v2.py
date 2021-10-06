
def login(users):

    while True:
        username = input("User: ")
        password = input("Password: ")

        if username in users.keys(): # om användarnamnet finns i keys
            if password == users[username]: # om lösenordet matchar användarnamnets lösen
                print(f"\nWelcome {username}")
                break
        print("\nInvalid username or password\n")


users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user1 = login(users1)
print(f"Welcome {user1}")

users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"Welcome {user2}")