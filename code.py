import random

items = []

while True:
    x = input("Enter: ")
    if x == "start":
        if len(items) <= 1:
            print("Nothing in list.")
        else:
            randomnumber = random.randint(-1, len(items) - 2)
            print(items, items[randomnumber]), items.pop(randomnumber)
    elif x in items:
        items.remove(x)
        print(items)
    else:
        items.append(x)
        print(items)
