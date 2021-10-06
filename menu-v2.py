
def menu(title, prompt, options):
    
    print(title,"\n")
    for key in options.keys():
        print(f"{key}) {options[key]}")

    print()

    ans = ""
    while ans not in options.keys(): # Loopar input tills man ger giltig input
        ans = input(f"{prompt}")
    
    return ans





options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
opt1 = menu("Select an action", "Action: ", options1)
#print(f"You selected action {opt1}) {options1[opt1]}")
print()

options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"You selected option {opt2}) {options2[opt2]}")