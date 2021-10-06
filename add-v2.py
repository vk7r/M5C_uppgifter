
def add(prompt, strings):
    lst = strings

    new_el = input(prompt)
    lst.append(new_el)

    return lst


ducks = ["Huey", "Dewey", "Louie"]

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()

# Test of the function add with the list composers.

composers = ["Mozart", "Bach"]
print(f" Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f" Composers: {composers}")
print()