
def tire2_list(cart, rb):
    import Error_Func
    f = open("tire2_inventory.txt", "r")
    rs = f.readlines()
    f.close()
    print(f"\n\033[34m{'*' * 100}\033[0m")
    print("\n\033[92m" + "------ 2 Wheeler Tires Inventory ------".center(100) + "\n\033[0m")

    for r in rs[1:]:
        var = r.strip().split("|")
        print(f"\033[93m[{var[0]}] - {var[1]} | Price: ₱{var[2]} | Stock: {var[3]}\033[0m")

    print("\n\033[91mTo Exit back to main menu type, [0]\n")

    id = str(input('\033[95mEnter the number for the item you wish to purchase, or type [0] to return to the category list: \033[0m')).strip()

    if id == '0':
        print("\033[93mReturning to category menu...\033[0m")
        return 'back'  # Return to Main Menu directly

    if not id.isnumeric():
        print("\n\033[31mInvalid item ID.\nMust be a number.\033[0m")
        return 'Lacking'

    # Check if ID exists
    found = False  # used to trigger Invalid item ID error
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            found = True
            break

    if not found:
        print("\033[31mInvalid item ID.\nSelected item ID does not exist.\033[0m")
        return 'Lacking'  # Loops back to item listing

    # Item Quantity Question
    while True:
        while True:
            order = input("\033[95mEnter the quantity of items you wish to purchase: \033[0m").strip()
            next = Error_Func.buy(order)
            if next == 'break':
                break
            elif next == 'continue':
                continue

        quantity = int(order)
        label = price = stock = value = None  # Used to define variables
        # Find item
        for r in rs[1:]:
            var = r.strip().split("|")
            if var[0].strip() == id.strip():
                label = var[1]
                price = int(var[2])
                stock = int(var[3])
                if quantity > stock:
                    print("\n\033[31mNot enough stock.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\n\033[0m")
                    value = 'More'
                break
        if value == 'More':
            continue

        else: # Add to cart
            cart.append({
                "category": "Accessories",
                "id": id,
                "name": label,
                "qty": quantity,
                "price": price
            })
            break

    rb.append({"file": "tire2_inventory.txt", "id": id, "qty": quantity}) #Inventory Rollback

    # Update inventory
    upr = [rs[0]]
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            var[3] = str(int(var[3]) - quantity)
        upr.append("|".join(var) + "\n")

    f = open("tire2_inventory.txt", "w")
    f.writelines(upr)
    f.close()

    print(f"\n\033[96mAdded {quantity}x {label} to cart.\033[0m")

def tire4_list(cart, rb):
    import Error_Func
    f = open("tire4_inventory.txt", "r")
    rs = f.readlines()
    f.close()
    print(f"\n\033[34m{'*' * 100}\033[0m")
    print("\n\033[92m" + "------ 4 Wheeler Tires Inventory ------".center(100) + "\n\033[0m")

    for r in rs[1:]:
        var = r.strip().split("|")
        print(f"\033[93m[{var[0]}] - {var[1]} | Price: ₱{var[2]} | Stock: {var[3]}\033[0m")

    print("\n\033[91mTo Exit back to main menu type, [0]\n")

    id = str(input('\033[95mEnter the number for the item you wish to purchase, or type [0] to return to the category list: \033[0m')).strip()

    if id == '0':
        print("\033[93mReturning to category menu...\033[0m")
        return 'back'  # Return to Main Menu directly

    if not id.isnumeric():
        print("\n\033[31mInvalid item ID.\nMust be a number.\033[0m")
        return 'Lacking'

    # Check if ID exists
    found = False  # used to trigger Invalid item ID error
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            found = True
            break

    if not found:
        print("\033[31mInvalid item ID.\nSelected item ID does not exist.\033[0m")
        return 'Lacking'  # Loops back to item listing

    # Item Quantity Question
    while True:
        while True:
            order = input("\033[95mEnter the quantity of items you wish to purchase: \033[0m").strip()
            next = Error_Func.buy(order)
            if next == 'break':
                break
            elif next == 'continue':
                continue

        quantity = int(order)
        label = price = stock = value = None  # Used to define variables
        # Find item
        for r in rs[1:]:
            var = r.strip().split("|")
            if var[0].strip() == id.strip():
                label = var[1]
                price = int(var[2])
                stock = int(var[3])
                if quantity > stock:
                    print("\n\033[31mNot enough stock.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\n\033[0m")
                    value = 'More'
                break
        if value == 'More':
            continue

        else: # Add to cart
            cart.append({
                "category": "Accessories",
                "id": id,
                "name": label,
                "qty": quantity,
                "price": price
            })
            break

    rb.append({"file": "tire4_inventory.txt", "id": id, "qty": quantity}) #Inventory Rollback

    # Update inventory
    upr = [rs[0]]
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            var[3] = str(int(var[3]) - quantity)
        upr.append("|".join(var) + "\n")

    f = open("tire4_inventory.txt", "w")
    f.writelines(upr)
    f.close()

    print(f"\n\033[96mAdded {quantity}x {label} to cart.\033[0m")

def parts_list(cart, rb):
    import Error_Func
    f = open("parts_inventory.txt", "r")
    rs = f.readlines()
    f.close()
    print(f"\n\033[34m{'*' * 100}\033[0m")
    print("\n\033[92m" + "------ Automotive Parts Inventory ------".center(100) + "\n\033[0m")

    for r in rs[1:]:
        var = r.strip().split("|")
        print(f"\033[93m[{var[0]}] - {var[1]} | Price: ₱{var[2]} | Stock: {var[3]}\033[0m")

    print("\n\033[91mTo Exit back to main menu type, [0]\n")

    id = str(input('\033[95mEnter the number for the item you wish to purchase, or type [0] to return to the category list: \033[0m')).strip()

    if id == '0':
        print("\033[93mReturning to category menu...\033[0m")
        return 'back'  # Return to Main Menu directly

    if not id.isnumeric():
        print("\n\033[31mInvalid item ID.\nMust be a number.\033[0m")
        return 'Lacking'

    # Check if ID exists
    found = False  # used to trigger Invalid item ID error
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            found = True
            break

    if not found:
        print("\033[31mInvalid item ID.\nSelected item ID does not exist.\033[0m")
        return 'Lacking'  # Loops back to item listing

    # Item Quantity Question
    while True:
        while True:
            order = input("\033[95mEnter the quantity of items you wish to purchase: \033[0m").strip()
            next = Error_Func.buy(order)
            if next == 'break':
                break
            elif next == 'continue':
                continue

        quantity = int(order)
        label = price = stock = value = None  # Used to define variables
        # Find item
        for r in rs[1:]:
            var = r.strip().split("|")
            if var[0].strip() == id.strip():
                label = var[1]
                price = int(var[2])
                stock = int(var[3])
                if quantity > stock:
                    print("\n\033[31mNot enough stock.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\n\033[0m")
                    value = 'More'
                break
        if value == 'More':
            continue

        else: # Add to cart
            cart.append({
                "category": "Accessories",
                "id": id,
                "name": label,
                "qty": quantity,
                "price": price
            })
            break

    rb.append({"file": "parts_inventory.txt", "id": id, "qty": quantity}) #Inventory Rollback

    # Update inventory
    upr = [rs[0]]
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            var[3] = str(int(var[3]) - quantity)
        upr.append("|".join(var) + "\n")

    f = open("parts_inventory.txt", "w")
    f.writelines(upr)
    f.close()

    print(f"\n\033[96mAdded {quantity}x {label} to cart.\033[0m")

def access_list(cart, rb):
    import Error_Func
    f = open("access_inventory.txt", "r")
    rs = f.readlines()
    f.close()
    print(f"\n\033[34m{'*' * 100}\033[0m")
    print("\n\033[92m" + "------ Accessories Inventory ------".center(100) + "\n\033[0m")

    for r in rs[1:]:
        var = r.strip().split("|")
        print(f"\033[93m[{var[0]}] - {var[1]} | Price: ₱{var[2]} | Stock: {var[3]}\033[0m")

    print("\n\033[91mTo Exit back to main menu type, [0]\n")

    id = str(input('\033[95mEnter the number for the item you wish to purchase, or type [0] to return to the category list: \033[0m')).strip()

    if id == '0':
        print("\033[93mReturning to category menu...\033[0m")
        return 'back'  # Return to Main Menu directly

    if not id.isnumeric():
        print("\n\033[31mInvalid item ID.\nMust be a number.\033[0m")
        return 'Lacking'

    # Check if ID exists
    found = False  # used to trigger Invalid item ID error
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            found = True
            break

    if not found:
        print("\033[31mInvalid item ID.\nSelected item ID does not exist.\033[0m")
        return 'Lacking'  # Loops back to item listing

    # Item Quantity Question
    while True:
        while True:
            order = input("\033[95mEnter the quantity of items you wish to purchase: \033[0m").strip()
            next = Error_Func.buy(order)
            if next == 'break':
                break
            elif next == 'continue':
                continue

        quantity = int(order)
        label = price = stock = value = None  # Used to define variables
        # Find item
        for r in rs[1:]:
            var = r.strip().split("|")
            if var[0].strip() == id.strip():
                label = var[1]
                price = int(var[2])
                stock = int(var[3])
                if quantity > stock:
                    print("\n\033[31mNot enough stock.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\n\033[0m")
                    value = 'More'
                break
        if value == 'More':
            continue

        else: # Add to cart
            cart.append({
                "category": "Accessories",
                "id": id,
                "name": label,
                "qty": quantity,
                "price": price
            })
            break

    rb.append({"file": "access_inventory.txt", "id": id, "qty": quantity}) #Inventory Rollback

    # Update inventory
    upr = [rs[0]]
    for r in rs[1:]:
        var = r.strip().split("|")
        if var[0].strip() == id.strip():
            var[3] = str(int(var[3]) - quantity)
        upr.append("|".join(var) + "\n")

    f = open("access_inventory.txt", "w")
    f.writelines(upr)
    f.close()

    print(f"\n\033[96mAdded {quantity}x {label} to cart.\033[0m")

