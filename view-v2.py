
def view(description, string):
    
    print(f"{description}\n")
    n = 1
    for name in string:
        print(f"{n}) {name}")
        n += 1
    
    



names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

view("Lista med namn", names)
print()
view("Lista med djur", animals)