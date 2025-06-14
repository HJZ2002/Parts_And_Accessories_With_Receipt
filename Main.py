import Catalog
import CartCalc
import Error_Func
import time
import sys

print("SELF REMINDER")
print("Feature prioritization:")
print("Tweaking of Cart Summary...Also add Payment in cart after confirming purchase\nDouble check text... make it coherent and make sense...better explain things\nItem removal system!!!\nerror coding needs additional error checks for more specificity")
print("Phone Number System... Error Coding needs to be reworked \n Create Functions for Error Coding to simplify. 1 for y or n, 1 for number, 1 for category, 1 for numbers... and more.")
print("When code is finished, ADD time commands to add wait time... Stylistic choice")
print("Error Code for Inventory needs fixing...\nCart Summary needs to be cleaned (Organize it)")



print(f"\n\033[34m{'*' * 100}\033[0m")
print("\n\033[92m" + "Autotread: Tires and Parts".center(100) + "\033[0m")
print(f"\n\033[34m{'*' * 100}\033[0m")
print(f"\n\033[92m" + "Welcome to Autotread, your local Tires and Automobile parts Shopping List".center(100) + "\033[0m")
print("\n\033[92m" + "Feel free to explore the different listings we have to offer".center(100) + "\033[0m")
print("\033[93m" + "Tires    :    Automobile Parts    :    Accessories".center(100) + "\033[0m")



cart = [] # Shared cart for the session
rb = [] # Used to allow for inventory rollback, upon order cancellation or End of session
while True:

    go_menu = False # Activate Browse Category Question

    #MAIN MENU
    print(f"\n\033[34m{'*' * 100}\033[0m")
    print("\n\033[92m" + "With Autotread you'll be able to choose from a varied selection of items and choose how many you".center(100) + "\033[0m")
    print("\033[92m" + "wish to purchase. Just type the appropriate number shown in between the '[]' to select".center(100) + "\033[0m")
    print("\033[92m" + "the item or category you want.".center(100) + "\n\033[0m")


    Checkout = Catalog.catalogs(cart, rb)  # This returns control once user finishes one interaction

    #Checkout
    while True: #checkout - 4 - CHECKOUT, check - 0 - END

        if Checkout == 'checkout' or Checkout == 'check':

            if not cart:  # End Session
                Catalog.restore(rb)
                print(cart)
                print("\033[95mCart is empty. Ending Session.\033[0m")
                print("\n\033[92mThank you for using Autotread! Please come again.\033[0m")
                sys.exit()

            elif cart and Checkout == 'check':  # End Session and Restore Inventory

                Catalog.restore(rb)
                print(cart)
                print("\033[95mCart has been emptied. All items in cart have been returned.\033[0m")
                print("\n\033[92mThank you for using Autotread! Please come again.\033[0m")
                sys.exit()

            else:
                print("\033[93mProceeding to checkout...\033[0m")
                # time.sleep(2)
                # Finalize Cart
                cancel, total, change, cash = CartCalc.final_cart(cart)
                if cancel == 'b':
                    go_menu = True  # Deactivate Browse Category Question
                    break
                # Finalize User data
                cname, contact = CartCalc.user_data()
                # Final Checkout
                CartCalc.receipt(cart, cname, contact, change, cash, total)
                sys.exit()
            break

        elif Checkout == 'back':
            break  # Return to main menu silently

        else:
            break


    #Browse more categories?
    while not go_menu:
        if Checkout == 'back':
            break
        y_or_n = input("\n\033[95mWould you like to browse another category? type 'y' for yes and type 'n' to proceed to checkout: \033[0m").lower().strip()
        if y_or_n == 'y':
            break

        elif y_or_n == 'n':
            while True:
                # Confirmation Question before going to checkout
                y_or_n = input("\n\033[91mAre you sure you would like to go to checkout? type 'y' for yes and type 'n' to return to main menu: \033[0m").strip()
                if y_or_n == 'n':
                    print("\n\033[93mReturning to category menu...\033[0m")
                    go_menu = True  # Deactivate Browse Category Question
                    break

                elif y_or_n == 'y':
                    if not cart:  # End Session
                        Catalog.restore(rb)
                        print(cart)
                        print("\033[95mCart is empty. Ending Session.\033[0m")
                        print("\n\033[92mThank you for using Autotread! Please come again.\033[0m")
                        sys.exit()

                    elif cart and Checkout == 'check':  # End Session and Restore Inventory
                        Catalog.restore(rb)
                        print(cart)
                        print("\033[95mCart has been emptied. All items in cart have been returned.\033[0m")
                        print("\n\033[92mThank you for using Autotread! Please come again.\033[0m")
                        sys.exit()

                    # Checkout
                    else:
                        print("\033[93mProceeding to checkout...\033[0m")
                        # time.sleep(2)
                        # Finalize Cart
                        cancel, total, change, cash = CartCalc.final_cart(cart)
                        if cancel == 'b':
                            go_menu = True  # Deactivate Browse Category Question
                            break
                        # Finalize User data
                        cname, contact = CartCalc.user_data()
                        # Final Checkout
                        CartCalc.receipt(cart, cname, contact, change, cash, total)
                        sys.exit()
                    break
                else:
                    # Check for Error Inputs
                    Error_Func.y_n(y_or_n)

        else:
            # Check for Error Inputs
            Error_Func.y_n(y_or_n)
