muffins = 10
cupcakes = 10

item = input("Enter muffin, cupcake, or 0 to finish: ")

while item != "0":
    if item == "muffin":
        if muffins > 0:
            muffins = muffins - 1
        else:
            print("Out of stock")

    elif item == "cupcake":
        if cupcakes > 0:
            cupcakes = cupcakes - 1
        else:
            print("Out of stock")

    item = input("Enter muffin, cupcake, or 0 to finish: ")

print("muffins:", muffins, "cupcakes:", cupcakes)
