import random
restaurants = ["tacobell","krustykrab","subway"]
menu_tacobell = ["taco","burrito","crunchwrap","water","soda"]
menu_krustykrab = ["Kraby Patty","Krusty Deluxe","Coral Bits","water","soda"]
menu_subway = ["Black forest ham sandwhich","Steak and Cheese Sandwhich","Chicken Terriyaki Sandwhich","water","soda"]
x=input("Which restaurant?"+str(restaurants))

if x=="tacobell":
    print(menu_tacobell)
    print(menu_tacobell[random.randrange(len(menu_tacobell))])
if x=="krustykrab":
    print(menu_krustykrab)
    print(menu_krustykrab[random.randrange(len(menu_krustykrab))])
if x=="subway":
    print(menu_subway)
    print(menu_subway[random.randrange(len(menu_subway))])