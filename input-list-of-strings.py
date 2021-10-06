
def add(prompt, strings):
    lst = strings

    new_el = input(prompt)
    lst.append(new_el)

    return lst

def view(description, string):
    
    print(f"{description}\n")
    n = 1
    for name in string:
        print(f"{n}) {name}")
        n += 1


strings = []
n = 5

for x in range(5):
    add("Lägg till en sträng: ", strings)
    print()

view(f"Du har matat in följande {n} strängar:", strings)