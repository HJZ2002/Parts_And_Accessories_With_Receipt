
def catalogs(cart, rb):

    import Inventory
    import Error_Func

    # Category Selection
    while True:
        #MAIN MENU
        print("\n\033[92mTo begin, please choose a category below or type [0] to end the session.\n\033[0m")
        print("\033[93mFor Tires please type [1]\033[0m")
        print("\033[93mFor Automobile Parts please type [2]\033[0m")
        print("\033[93mFor Accessories please type [3]\n\033[0m")


        if cart:  # Only shows if cart has items
            print("\033[93mTo Proceed to Checkout please type [4]\033[0m")

        print("\033[91mTo End the session please type [0]\033[0m")
        catalog_p1 = str(input("\n\033[95mWhere would you like your Journey to begin: \033[0m")).strip()

        #ENDS SESSION
        if catalog_p1 == '0':
            #Ask for confirmation
            while True:
                y_or_n = input("\n\033[91mAre you sure you would like to end the session? type 'y' to continue and type 'n' to return to main menu: \033[0m").strip()
                if y_or_n == 'y':
                    return 'check'

                elif y_or_n == 'n':
                    return 'back'
                else:
                    # Check for Error Inputs
                    Error_Func.y_n(y_or_n)



        #Tires
        elif catalog_p1 == '1':
            while True:
                print(f"\n\033[34m{'*' * 100}\033[0m")
                print("\n\033[93mFor Two Wheel Vehicle Tires please type [1]\033[0m")
                print("\033[93mFor Four Wheel Vehicle Tires please type [2]\033[0m")
                print("\n\033[91mTo Exit back to main menu, type [0]\033[0m")
                catalog_p2 = str(input("\n\033[95mWhat would you like to check out first: \033[0m")).strip()

                # Display 2Tire inventory
                if catalog_p2 == '1':
                    print("\n\033[93mYou selected Two Wheel Vehicle Tires...\033[0m")
                    #time.sleep(1)
                    while True:
                        yorn = Inventory.tire2_list(cart, rb)  # Checks if it should ask for checkout or return to main menu
                        if yorn == 'back':
                            break
                        elif yorn == 'Lacking':
                            continue
                        else:
                            return



                # Display 4Tire inventory
                elif catalog_p2 == '2':
                    print("\n\033[93mYou selected Four Wheel Vehicle Tires...\033[0m")
                    #time.sleep(1)
                    while True:
                        yorn = Inventory.tire4_list(cart,
                                                    rb)  # Checks if it should ask for checkout or return to main menu
                        if yorn == 'back':
                            break
                        elif yorn == 'Lacking':
                            continue
                        else:
                            return


                elif catalog_p2 == '0':
                    return 'back'  # Back to main category menu

                # Check for Input Errors
                elif catalog_p2.isdigit():
                    print("\n\033[31mInput is not for any existing category.", "\nPlease try again.\033[0m")


                elif catalog_p2.isalpha():
                    print("\n\033[31mInput must be numeric.", "\nPlease try again.\033[0m")

                else:
                    print("\n\033[31mInput must be a number from 0-2.", "\nPlease try again.\033[0m")

        #Parts
        elif catalog_p1 == '2':
            print("\n\033[93mDisplaying Automotive Parts Inventory...\033[0m")
            #time.sleep(1)
            while True:
                yorn = Inventory.parts_list(cart, rb)  # Checks if it should ask for checkout or return to main menu
                if yorn == 'back':
                    return 'back'
                elif yorn == 'Lacking':
                    continue
                else:
                    return

        # Accessories
        elif catalog_p1 == '3':
            print("\n\033[93mDisplaying Accessories Inventory...\033[0m")
            #time.sleep(1)
            while True:
                yorn = Inventory.access_list(cart, rb)  # Checks if it should ask for checkout or return to main menu
                if yorn == 'back':
                    return 'back'
                elif yorn == 'Lacking':
                    continue
                else:
                    return


        elif catalog_p1 == '4' and cart:
            while True:
                y_or_n = input("\n\033[91mAre you sure you would like to go to checkout? type 'y' for yes and type 'n' to return to main menu: \033[0m").strip()
                if y_or_n == 'n':
                    print("\n\033[93mReturning to category menu...\033[0m")
                    return 'back'  # Return to Main Menu directly

                elif y_or_n == 'y':
                    return 'checkout'
                else:
                    # Check for Error Inputs
                    Error_Func.y_n(y_or_n)


        # Check for Input Errors
        elif catalog_p1.isdigit():
            print("\n\033[31mInput is not for any existing category.", "\nPlease try again.\033[0m")
            print(f"\n\033[34m{'*' * 100}\033[0m")

        elif catalog_p1.isalpha():
            print("\n\033[31mInput must be numeric.", "\nPlease try again.\033[0m")
            print(f"\n\033[34m{'*' * 100}\033[0m")

        else:
            print("\n\033[31mInput must be a number.", "\nPlease try again.\033[0m")
            print(f"\n\033[34m{'*' * 100}\033[0m")



def restore(rerolls):
    for reroll in rerolls:
        file = reroll["file"]
        item_id = reroll["id"]
        qty_restore = reroll["qty"]

        with open(file, "r") as f:
            rs = f.readlines()

        upr = [rs[0]]
        for r in rs[1:]:
            parts = r.strip().split("|")
            if parts[0].strip() == item_id:
                parts[3] = str(int(parts[3]) + qty_restore)
            upr.append("|".join(parts) + "\n")

        with open(file, "w") as f:
            f.writelines(upr)

