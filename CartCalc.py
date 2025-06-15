from Receipt import Receipt
import datetime
import random
import os
def final_cart(cart):
    import Error_Func
    finale = {}
    total = 0

    #Combine Items into 1 set
    for var in cart:
        label = var['name']
        qty = var['qty']
        price = var['price']

        if label in finale:
            finale[label]['qty'] += qty
        else:
            finale[label] = {'qty': qty, 'price': price}

    print(f"\n\033[34m{'*' * 100}\033[0m")
    print("\n\033[92m" + "======= CART SUMMARY =======".center(100) + "\033[0m")
    for label, var in finale.items():
        subtotal = var['qty'] * var['price']
        print(f"\033[93m                              {label} - {var['qty']} x ₱{var['price']:,.2f} = ₱{subtotal:,.2f}         \033[0m")
        total += subtotal

    while True:
        # Payment Amount
        print(f"\n\033[96mTOTAL AMOUNT DUE: ₱{total:,.2f}\033[0m")
        cash = input("\n\033[95mPlease Enter the amount you will be paying for today: ")
        #Make cash an integer
        if cash.isnumeric():
            cash = int(cash)
            if cash < total:
                print("\n\033[31mUnfortunately that amount is not enough to pay for your TOTAL.\033[0m")
                print(f"\n\033[34m{'*' * 100}\033[0m")
                print('\n\033[92mIf you want to want to reduce your cart return to the main menu and select the\n"Remove Item" category.\033[0m')
                while True:
                    y_or_n = input("\n\033[95mType 'y' to return to main menu and type 'n' if you would like to adjust the amount\nyou will be paying for today: \033[0m").strip()
                    if y_or_n == 'n':
                        print(f"\n\033[34m{'*' * 100}\033[0m")
                        break
                    elif y_or_n == 'y':
                        print("\n\033[93mReturning to category menu...\033[0m")
                        return 'b000'  # Return to Main Menu directly

                    # Check for Error Inputs
                    Error_Func.y_n(y_or_n)




            elif cash >= total:
                break

            else:
                print("\n\033[31mAmount must be a number.", "\nPlease try again.\033[0m")
                print(f"\n\033[34m{'*' * 100}\033[0m")

        elif cash.isalpha():
            # Error Coding
            while True:
                # Make cash into string for error checking
                str_cash = str(cash)
                if str_cash.isalpha():
                    print("\n\033[31mAmount must be a number.\033[0m")
                    print("\033[31mPlease try again.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\033[0m")
                    break

                elif str_cash < '0':
                    print("\n\033[31mAmount must be positive.\033[0m")
                    print("\033[31mPlease try again.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\033[0m")
                    break

                else:
                    print("\n\033[31mAmount must be a number.\033[0m")
                    print("\033[31mPlease try again.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\033[0m")
                    break
        else:
            print("\n\033[31mAmount must be a number.", "\nPlease try again.\033[0m")
            print(f"\n\033[34m{'*' * 100}\033[0m")

    #Calculate Change for Receipt
    change = cash - total
    print(f"\n\033[34m{'*' * 100}\033[0m")

    print(f"\n\033[96mTotal Amount Paid: ₱{cash:,.2f}\033[0m")
    print(f"\033[96mTotal Change: ₱{change:,.2f}\033[0m")

    while True:
        # Confirmation to proceed
        y_or_n = input("\n\033[95mDo you wish to confirm you're purchase? type 'y' for yes and type 'n' to return to the main menu: \033[0m").strip()
        if y_or_n == 'n':
            print("\n\033[93mReturning to category menu...\033[0m")
            return 'b000'  # Return to Main Menu directly
        elif y_or_n == 'y':
            return 'c', total, change, cash

        # Check for Error Inputs
        Error_Func.y_n(y_or_n)

def user_data():
    import Error_Func

    print(f"\n\033[34m{'*' * 100}\n\033[0m")
    print("\033[92m" + "Please input the necessary data for us to print out you're receipt.".center(100) + "\033[0m")
    print("\033[92m" + "Rest assured, all data will be used strictly for the storing and printing of you're receipt.".center(100) + "\033[0m")
    while True:
        fname = str(input("\n\033[93mPlease provide your first name: \033[0m")).strip()
        lname = str(input("\033[93mPlease provide your last name: \033[0m")).strip()

        while True:
            phone = input("\033[93mPlease provide your phone number (e.g. 0991 911 9111): \033[0m")

            # Remove special characters, typically used.
            filler = "=-+|/&@!* "
            for series in filler:
                phone = phone.replace(series, '')

            # Account for national number inputs
            if len(phone) >= 2 and phone[0:2] == '63':
                phone = '0' + phone[2:]

            # Check for user input errors
            if not phone:
                print("\n\033[31mNo Input Detected.\033[0m")
                print("\033[31mPlease Try Again.\033[0m")
                print(f"\n\033[34m{'*' * 100}\n\033[0m")

            elif not phone.isnumeric():
                print("\n\033[31mPhone number must be numeric.\033[0m")
                print("\033[31mPlease Try Again.\033[0m")
                print(f"\n\033[34m{'*' * 100}\n\033[0m")

            elif len(phone) != 11:
                if len(phone) >= 11:
                    print("\n\033[31mPhone number is more than [11] digits.\033[0m")
                    print("\033[31mPhone number must be exactly [11] digits.\033[0m")
                    print("\033[31mPlease Try Again.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\n\033[0m")

                elif len(phone) <= 11:
                    print("\n\033[31mPhone number is less than [11] digits.\033[0m")
                    print("\033[31mPhone number must be exactly [11] digits.\033[0m")
                    print("\033[31mPlease Try Again.\033[0m")
                    print(f"\n\033[34m{'*' * 100}\n\033[0m")

            elif phone[0] != '0':
                print("\n\033[31mPhone number must start with '0'.\033[0m")
                print("\n\033[31mPlease Try Again.\033[0m")
                print(f"\n\033[34m{'*' * 100}\n\033[0m")

            elif phone[1] != '9':
                print("\n\033[31mPhone number's second number must be '9'.\033[0m")
                print("\033[31mPlease Try Again.\033[0m")
                print(f"\n\033[34m{'*' * 100}\n\033[0m")

            else:
                # Phone Finalization
                cname = (fname + " " + lname)
                contact = str(phone[0:4] + " " + phone[4:7] + " " + phone[7:11])
                print(f"\n\033[34m{'*' * 100}\033[0m")
                print("\n\033[92m" + "To complete the processing of your receipt, please confirm the following information.".center(100) + "\033[0m")
                print("\n\033[92m" + "Please confirm that this is your phone number in the standard Philippine".center(100) + "\033[0m")
                print("\033[92m" + "national format (e.g. 0991 911 9111). As well as your full name.".center(100) + "\033[0m")
                print("\n\033[96mFull Name:", cname + "\033[0m")
                print("\033[96mPhone Number:", contact + "\033[0m")

                while True:
                    y_or_n = input("\n\033[95mIf the information is correct, type 'y' to complete your transaction and type 'n'\nif you wish to change your name and contact number: \033[0m").strip()
                    if y_or_n == 'y':
                        return cname, contact
                    elif y_or_n == 'n':
                        print(f"\n\033[34m{'*' * 100}\033[0m")
                        break
                    else:
                        # Check for Error Inputs
                        Error_Func.y_n(y_or_n)

                break

def receipt(cart, cname, contact, change, cash, total):
    # Create and save receipt
    receipt = Receipt(cart, cname, contact, total, cash, change)
    receipt.save_to_file()
    receipt.print_receipt()

    # Make Receipt folder
    recp_fold = "Receipts"
    os.makedirs(recp_fold, exist_ok=True)

    # Clean up number
    filler = " "
    pcontact = contact.strip()
    for series in filler:
        pcontact = contact.replace(series, '')

    # Clean up name
    filler = " "
    pname = cname.strip()
    for series in filler:
        pname = cname.replace(series, '')

    # Title of Receipt and file location
    now = datetime.datetime.now()
    order_num = random.randint(1000000, 9999999)
    timestamp = now.strftime("%Y-%m-%d_%H:%M")
    filename = (f"{pname}_{pcontact}_#{order_num}_{timestamp}").strip()
    filepath = os.path.join(recp_fold, filename + ".txt")

    finale = {}
    # Combine Items into 1 set
    for var in cart:
        label = var['name']
        qty = var['qty']
        price = var['price']
        if label in finale:
            finale[label]['qty'] += qty
        else:
            finale[label] = {'qty': qty, 'price': price}

    # Receipt contents
    print(f"\n\n\n\033[94m{'=' * 100}\033[0m")
    print("\033[92m" + "AUTOTREAD RECEIPT".center(100) + "\033[0m")
    print(f"\033[94m{'=' * 100}\033[0m")
    print(f"\033[92mCustomer Name : {cname}\033[0m")
    print(f"\033[92mPhone Number  : {contact}\033[0m")
    print(f"\033[92mOrder Number  : {order_num}\033[0m")
    print(f"\033[92mDate/Time     : {now.strftime('%B %d, %Y | %I:%M %p')}\033[0m")
    print(f"\033[94m{'-' * 100}\033[0m")
    print(f"\033[93m    {'Item':<35}{'Qty':<19}{'Price':<26}{'Subtotal'}\033[0m")
    print(f"\033[94m{'-' * 100}\033[0m")

    for label, var in finale.items():
        subtotal = var['qty'] * var['price']
        print(f"\033[93m{label:<40}{var['qty']:<18}₱{var['price']:<25,.2f}₱{subtotal:<12,.2f}\033[0m")

    print(f"\033[94m{'-' * 100}\033[0m")
    print(f"\033[96m{'TOTAL:':<84}₱{total:,.2f}\033[0m")
    print(f"\033[94m{'=' * 100}\033[0m")
    print(f"\033[96m{'Amount Paid:':<84}₱{cash:,.2f}\033[0m")
    print(f"\033[96m{'Change:':<84}₱{change:,.2f}\033[0m")
    print(f"\033[94m{'=' * 100}\033[0m")
    print(f"\033[92m{'Prepared by:':<15}\033[0m")
    print("\033[92m     Hosea James Zacarias\033[0m".ljust(30))
    print(f"\033[92m{'\nAuthorized by:':<15}\033[0m")
    print("\033[92m     Hosea James Zacarias\033[0m".ljust(30))
    print(f"\033[94m{'=' * 100}\033[0m")
    print(f"\033[92m{'Printed on :        ':>82}{now.strftime('%m-%d-%Y %H:%M')}\033[0m")
    print(f"\033[92m" + "Contact Us :           09XX-XXX-XXXX".rjust(98) + "\033[0m")
    print(f"\033[92m" + "Email Us   : autotread09XX@gmail.com".rjust(98) + "\033[0m")
    print(f"\033[94m{'=' * 100}\n\033[0m")
    print("\n\n\n\033[92mYour Receipt has been printed.\033[0m")
    print("\033[92mThank you for using Autotread! Please come again.\033[0m")

    # Receipt TXT contents
    user_recp = []
    user_recp.append(f"{'=' * 100}")
    user_recp.append("AUTOTREAD RECEIPT".center(100))
    user_recp.append(f"{'=' * 100}")
    user_recp.append(f"Customer Name: {cname}")
    user_recp.append(f"Phone Number : {contact}")
    user_recp.append(f"Order Number : {order_num}")
    user_recp.append(f"Date/Time    : {now.strftime('%B %d, %Y | %I:%M %p')}")
    user_recp.append(f"{'-' * 100}")
    user_recp.append(f"    {'Item':<35}{'Qty':<19}{'Price':<26}{'Subtotal'}")
    user_recp.append(f"{'-' * 100}")

    for label, var in finale.items():
        subtotal = var['qty'] * var['price']
        user_recp.append(f"{label:<40}{var['qty']:<18}₱{var['price']:<25,.2f}₱{subtotal:<12,.2f}")

    user_recp.append(f"{'-' * 100}")
    user_recp.append(f"{'TOTAL:':<84}₱{total:,.2f}")
    user_recp.append(f"{'=' * 100}")
    user_recp.append(f"{'Amount Paid:':<84}₱{cash:,.2f}")
    user_recp.append(f"{'Change:':<84}₱{change:,.2f}")
    user_recp.append(f"{'=' * 100}")
    user_recp.append(f"{'Prepared by:':<15}")
    user_recp.append("    Hosea James Zacarias\n".ljust(30))
    user_recp.append(f"{'Authorized by:':<15}")
    user_recp.append("     Hosea James Zacarias".ljust(30))
    user_recp.append(f"{'=' * 100}")
    user_recp.append(f"{'Printed on :        ':>82}{now.strftime('%m-%d-%Y %H:%M')}")
    user_recp.append(f"Contact Us :           09XX-XXX-XXXX".rjust(98))
    user_recp.append(f"Email Us   : autotread09XX@gmail.com".rjust(98))
    user_recp.append(f"{'=' * 100}\n")


