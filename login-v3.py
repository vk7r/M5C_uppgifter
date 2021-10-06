

def menu(title, prompt, options):
    
    print(title,"\n")
    for key in options.keys():
        print(f"{key}) {options[key]}")

    print()

    ans = ""
    while ans not in options.keys(): # Loopar input tills man ger giltig input
        ans = input(f"{prompt}")
    
    return ans



def login(users):

    while True:
        username = input("User: ")
        password = input("Password: ")

        if username in users.keys(): # om användarnamnet finns i keys
            if password == users[username]: # om lösenordet matchar användarnamnets lösen
                print(f"\nWelcome {username}")
                return username

        print("\nInvalid username or password\n")
        ans = menu("","Option: ",{"r":"Try again", "q":"Quit"})

        if ans == "q":
            return None


users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

user = login(users)