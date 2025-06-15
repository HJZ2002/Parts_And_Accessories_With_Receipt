import os
import random
from datetime import datetime


class Receipt:
    def __init__(self, cart, customer_name, contact_number, total_amount, amount_paid, change):
        """
        Initialize receipt with transaction details

        Args:
            cart: List of items in cart (each item is a dict with name, qty, price)
            customer_name: Full name of customer
            contact_number: Formatted phone number
            total_amount: Total amount due
            amount_paid: Amount paid by customer
            change: Change to be returned
        """
        self.cart = cart
        self.customer_name = customer_name
        self.contact_number = contact_number
        self.total_amount = total_amount
        self.amount_paid = amount_paid
        self.change = change
        self.order_number = random.randint(1000000, 9999999)
        self.timestamp = datetime.now()
        self.receipt_folder = "Receipts"

        # Ensure receipts folder exists
        os.makedirs(self.receipt_folder, exist_ok=True)

    def generate_receipt_content(self):
        """Generate formatted receipt content as list of lines"""
        # Combine duplicate items in cart
        combined_items = {}
        for item in self.cart:
            name = item['name']
            if name in combined_items:
                combined_items[name]['qty'] += item['qty']
            else:
                combined_items[name] = {'qty': item['qty'], 'price': item['price']}

        # Format receipt lines
        lines = []
        lines.append(f"{'=' * 100}")
        lines.append("AUTOTREAD RECEIPT".center(100))
        lines.append(f"{'=' * 100}")
        lines.append(f"Customer Name: {self.customer_name}")
        lines.append(f"Phone Number : {self.contact_number}")
        lines.append(f"Order Number : {self.order_number}")
        lines.append(f"Date/Time    : {self.timestamp.strftime('%B %d, %Y | %I:%M %p')}")
        lines.append(f"{'-' * 100}")
        lines.append(f"    {'Item':<35}{'Qty':<19}{'Price':<26}{'Subtotal'}")
        lines.append(f"{'-' * 100}")

        # Add items to receipt
        for name, details in combined_items.items():
            subtotal = details['qty'] * details['price']
            lines.append(
                f"{name:<40}{details['qty']:<18}₱{details['price']:<25,.2f}₱{subtotal:<12,.2f}"
            )

        # Add totals and footer
        lines.append(f"{'-' * 100}")
        lines.append(f"{'TOTAL:':<84}₱{self.total_amount:,.2f}")
        lines.append(f"{'=' * 100}")
        lines.append(f"{'Amount Paid:':<84}₱{self.amount_paid:,.2f}")
        lines.append(f"{'Change:':<84}₱{self.change:,.2f}")
        lines.append(f"{'=' * 100}")
        lines.append(f"{'Prepared by:':<15}")
        lines.append(f"{'Prepared by:':<15}")
        lines.append("     Hosea James Zacarias ".ljust(30))
        lines.append(f"{'Authorized by:':<15}")
        lines.append("     Hosea James Zacarias ".ljust(30))
        lines.append(f"{'=' * 100}")
        lines.append(f"{'Printed on :        ':>82}{self.timestamp.strftime('%m-%d-%Y %H:%M')}")
        lines.append("Contact Us :           09XX-XXX-XXXX".rjust(98))
        lines.append("Email Us   : autotread09XX@gmail.com".rjust(98))
        lines.append(f"{'=' * 100}\n")

        return lines

    def save_to_file(self):
        """Save receipt to file in Receipts folder"""
        # Clean filename components
        clean_name = "".join(c if c.isalnum() else "_" for c in self.customer_name)
        clean_contact = "".join(c for c in self.contact_number if c.isdigit())

        filename = f"{clean_name}_{clean_contact}_#{self.order_number}_{self.timestamp.strftime('%Y-%m-%d_%H-%M')}.txt"
        filepath = os.path.join(self.receipt_folder, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(self.generate_receipt_content()))

        return filepath

    def print_receipt(self):
        """Print receipt to console with colors (matching your existing style)"""
        # Combine duplicate items in cart
        combined_items = {}
        for item in self.cart:
            name = item['name']
            if name in combined_items:
                combined_items[name]['qty'] += item['qty']
            else:
                combined_items[name] = {'qty': item['qty'], 'price': item['price']}

        # Print receipt with colors
        print(f"\n\n\n\033[94m{'=' * 100}\033[0m")
        print("\033[92m" + "AUTOTREAD RECEIPT".center(100) + "\033[0m")
        print(f"\033[94m{'=' * 100}\033[0m")
        print(f"\033[92mCustomer Name : {self.customer_name}\033[0m")
        print(f"\033[92mPhone Number  : {self.contact_number}\033[0m")
        print(f"\033[92mOrder Number  : {self.order_number}\033[0m")
        print(f"\033[92mDate/Time     : {self.timestamp.strftime('%B %d, %Y | %I:%M %p')}\033[0m")
        print(f"\033[94m{'-' * 100}\033[0m")
        print(f"\033[93m    {'Item':<35}{'Qty':<19}{'Price':<26}{'Subtotal'}\033[0m")
        print(f"\033[94m{'-' * 100}\033[0m")

        for name, details in combined_items.items():
            subtotal = details['qty'] * details['price']
            print(f"\033[93m{name:<40}{details['qty']:<18}₱{details['price']:<25,.2f}₱{subtotal:<12,.2f}\033[0m")

        print(f"\033[94m{'-' * 100}\033[0m")
        print(f"\033[96m{'TOTAL:':<84}₱{self.total_amount:,.2f}\033[0m")
        print(f"\033[94m{'=' * 100}\033[0m")
        print(f"\033[96m{'Amount Paid:':<84}₱{self.amount_paid:,.2f}\033[0m")
        print(f"\033[96m{'Change:':<84}₱{self.change:,.2f}\033[0m")
        print(f"\033[94m{'=' * 100}\033[0m")
        print(f"\033[92m{'Prepared by:':<15}\033[0m")
        print("\033[92m     Staff\033[0m".ljust(30))
        print(f"\033[92m{'\nAuthorized by:':<15}\033[0m")
        print("\033[92m     Staff\033[0m".ljust(30))
        print(f"\033[94m{'=' * 100}\033[0m")
        print(f"\033[92m{'Printed on :        ':>82}{self.timestamp.strftime('%m-%d-%Y %H:%M')}\033[0m")
        print(f"\033[92m" + "Contact Us :           09XX-XXX-XXXX".rjust(98) + "\033[0m")
        print(f"\033[92m" + "Email Us   : autotread09XX@gmail.com".rjust(98) + "\033[0m")
        print(f"\033[94m{'=' * 100}\n\033[0m")
        print("\n\n\n\033[92mYour Receipt has been printed.\033[0m")
        print("\033[92mThank you for using Autotread! Please come again.\033[0m")
