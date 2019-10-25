from tabel import Tabel
import csv
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    for i in inventory:
        print(i, ':', inventory.get(i))


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory.keys():
            inventory[i] = inventory.get(i) + 1
        else:
            inventory[i] = 1
    return inventory


def print_table(inventory, order=None):
    items = []
    count = []
    if order == None:
        for i in inventory:
            items.append(i)
            count.append(inventory.get(i))
    if order == "count,desc":
        inventory_desc = sorted(
            inventory.items(), key=lambda t: t[1], reverse=True)
        for j in inventory_desc:
            items.append(j[0])
            count.append(j[1])
    elif order == "count,asc":
        inventory_asc = sorted(
            inventory.items(), key=lambda t: t[1])
        for j in inventory_asc:
            items.append(j[0])
            count.append(j[1])
    tbl = Tabel([items,
                 count], columns=["Item name", "Count"])
    print(tbl)


def import_inventory(inventory, filename="import_inventory.csv"):
    with open('import_inventory.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line = []
        for l in csv_reader:
            line = l

    for i in line:
        if i in inventory.keys():
            inventory[i] = inventory.get(i) + 1
        else:
            inventory[i] = 1
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, 'w') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        inv1 = []
        for item, count in inv.items():
            for i in range(count):
                inv1.append(item)
        writer.writerow(inv1)


add_to_inventory(inv, dragon_loot)
display_inventory(inv)
print(import_inventory(inv))
print_table(inv, "count,desc")
export_inventory(inv)
