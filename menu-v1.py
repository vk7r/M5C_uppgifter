
options = {"a":"Add item", "l":"List items", "q":"Log out"}

print("""Select an action:  
  a) Add item
  l) List items
  q) Log out\n""")


ans = ""
while ans not in options.keys(): # Loopar input tills man ger giltig input
    ans = input("Option: ")
print(f"You selected item {ans}) {options[ans]}")

