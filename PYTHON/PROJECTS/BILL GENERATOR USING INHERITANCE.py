'''WE HAVING THE BASE MRP IN THE BILL WHICH CAN PRINT THE MRP AS PARENT CLASS
<1> GROCERIES : MRP + 5% CGST
<2> COSMETIC ITEMS : MRP + 18% GST
<3> CLOTHS : MRP + 18% GST + 5% CGST
'''
# creating the parent class having MRP
class MRP:
    def info(self, baseprice, item_name):
        self.item_name = item_name
        self.baseprice = baseprice

    def label(self):
        print(f'''
                ************ NEW INDIA SUPER MARKET ***********
                ************************************************''')

    def print_price(self):
        print(f'''
                : : : : : SELECTED ITEM : {self.item_name} : : : : :
                : : : : The MRP of the item : {self.baseprice} Rs : : : :''')


# <1> Groceries Child Class
class GROCERIES(MRP):
    def __init__(self, baseprice, item_name):
        super().info(baseprice, item_name)

    def print_price(self):
        super().print_price()
        base = self.baseprice
        gst = 0.05 * (self.baseprice)
        total = base + gst
        print(f'''
                ---------------{self.item_name} = {base} Rs ----------------
                                + 5% CGST [{gst} Rs]
                                = {total} Rs''')
        return total


# <2> Cosmetic Items
class COSITEMS(MRP):
    def __init__(self, baseprice, item_name):
        super().info(baseprice, item_name)

    def print_price(self):
        super().print_price()
        base = self.baseprice
        gst = 0.18 * (self.baseprice)
        total = base + gst
        print(f'''
                ---------------{self.item_name} = {base} Rs ----------------
                                + 18% GST [{gst} Rs]
                                = {total} Rs''')
        return total


# <3> Cloth items
class CLOTHITEMS(MRP):
    def __init__(self, baseprice, item_name):
        super().info(baseprice, item_name)

    def print_price(self):
        super().print_price()
        base = self.baseprice
        gst = 0.18 * (self.baseprice)
        cgst = 0.05 * (self.baseprice)
        total = base + gst + cgst
        print(f'''
                ---------------{self.item_name} = {base} Rs ----------------
                                + 18% GST [{gst} Rs]
                                + 5% CGST [{cgst} Rs]
                                = {total} Rs''')
        return total


# Class to calculate the total amount
class Total:
    def __init__(self):
        self.total = 0

    def calculate_total(self, items):
        self.total = sum(item.print_price() for item in items)

    def print_total(self):
        print(f'''
                ################ TOTAL = {self.total} Rs ##################
                ''')


# Function to take input from the user and assign it catagory
def get_item_input():
    item_name = input("Enter the product name: ")
    baseprice = float(input(f"Enter the MRP for {item_name}: Rs "))
    category = input("Enter the category (Groceries = 1, Cosmetics = 2, Clothes = 3): ").strip()

    if category == '1':
        return GROCERIES(baseprice, item_name)
    elif category == '2':
        return COSITEMS(baseprice, item_name)
    elif category == '3':
        return CLOTHITEMS(baseprice, item_name)
    else:
        print("Invalid category!")
        return None

# ASKING USER THAT HOW MANY ITEMS HE WANT TO ADD IN CART
n=int(input("Enter No of Products :"))
if __name__ == "__main__":
    # Get user input for N items
    items = []
    for i in range(n):
        print(f"\nEnter details for Item {i+1}:")
        item = get_item_input()
        if item:
            items.append(item)
    
    label1=MRP()
    label1.label()

    # Create the Total object and calculate the total
    final_total = Total()
    final_total.calculate_total(items)

    # Print the total amount
    final_total.print_total()
