
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}


while True:
    username = input("User: ")
    password = input("Password: ")

    if username in users.keys(): # om användarnamnet finns i keys
            if password == users[username]: # om lösenordet matchar användarnamnets lösen
                print(f"\nWelcome {username}")
                break
    print("\nInvalid username or password\n")