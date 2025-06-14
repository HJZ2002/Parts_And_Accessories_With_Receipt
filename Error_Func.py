#Input Functions for easier Error Output.

#Y or N error

def y_n(y_or_n):
    if y_or_n.isdigit():
        print("\n\033[31mInput is must not be numeric.", "\nPlease try again.\033[0m")
        print(f"\n\033[34m{'*' * 100}\033[0m")
    elif y_or_n.isalpha():
        print("\n\033[31mInput must be either 'y' or 'n'.", "\nPlease try again.\033[0m")
        print(f"\n\033[34m{'*' * 100}\033[0m")
    else:
        print("\n\033[31mInput must be either 'y' or 'n'.", "\nPlease try again.\033[0m")
        print(f"\n\033[34m{'*' * 100}\033[0m")

def buy(order):
    if order.isalpha():
        print("\n\033[31mInput cannot be a letter.\033[0m")
        print("\033[31mPlease try again.\033[0m")
        print(f"\n\033[34m{'*' * 100}\n\033[0m")
        return 'continue'
    elif order == '0':
        print("\n\033[31mInput must be more than 0.\033[0m")
        print("\033[31mPlease try again.\033[0m")
        print(f"\n\033[34m{'*' * 100}\n\033[0m")
        return 'continue'
    elif order < '0':
        print("\n\033[31mInput must be positive.\033[0m")
        print("\033[31mPlease try again.\033[0m")
        print(f"\n\033[34m{'*' * 100}\n\033[0m")
        return 'continue'
    elif order.isnumeric():
        return 'break'
    else:
        print("\n\033[31mInput must be a number.\033[0m")
        print("\033[31mPlease try again.\033[0m")
        print(f"\n\033[34m{'*' * 100}\n\033[0m")
        return 'continue'




