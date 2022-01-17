pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for top in pizza['toppings']:
    print("\t" + top)