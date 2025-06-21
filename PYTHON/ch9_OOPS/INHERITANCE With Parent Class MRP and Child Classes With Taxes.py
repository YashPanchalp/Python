'''WE HAVING THE BASE MRP IN THE BILL WHICH CAN PRINT THE MRP AS PARENT CLASS
<1> GROCERIES : MRP + 5% CGST
<2> COSMETIC ITEMS : MRP + 18% GST
<3> CLOTHS : MRP + 18% GST + 5% CGST
'''

#creating the parent class havng mrp
class MRP:

    def __init__(self, baseprice,item_name):
        self.item_name=item_name
        self.baseprice=baseprice

    def label(self):
        print(f'''
                ************ NEW INDIA SUPER MARCKET ***********
                ************************************************''')

    def print_price(self):
        print(f'''
                : : : : : SELCTERD ITEM : {self.item_name} : : : : :
                : : : : The MRP of the item : {self.baseprice} Rs : : : :''')

# <1> Groceries Child Class
class GROCERIES(MRP):

    def __init__(self, baseprice,item_name):
        super().__init__(baseprice,item_name)

    def print_price(self):
        super().print_price()
        base=self.baseprice
        gst= 0.05*(self.baseprice)
        total1=base + gst
        print(f'''
                ---------------{self.item_name} = {base} Rs ----------------
                                + 5% CGST [{gst}Rs]
                                = {total1} Rs''') 
        return total1

# <2> Cosmetic Items
class COSITEMS(MRP):

    def __init__(self, baseprice, item_name):
        super().__init__(baseprice, item_name)

    def print_price(self):
        super().print_price()
        base=self.baseprice
        gst= 0.18*(self.baseprice)
        total2=base + gst
        print(f'''
                ---------------{self.item_name} = {base} Rs ----------------
                                + 18% GST [{gst}Rs]
                                = {total2} Rs''') 
        return total2

# <3> Cloth items
class CLOTHITEMS(MRP):

    def __init__(self, baseprice, item_name):
        super().__init__(baseprice, item_name)

    def print_price(self):
        super().print_price()
        base=self.baseprice
        gst= 0.18*(self.baseprice)
        cgst=0.05*(self.baseprice)
        total3=base + gst
        print(f'''
                ---------------{self.item_name} = {base} Rs ----------------
                                + 18% GST [{gst}Rs]
                                + 5% CGST [{cgst}Rs]
                                = {total3} Rs''') 
        return total3

'''CREATE CLASS THAT PRINT TOTAL AMOUNT WITH CHILD CLASSES
    1 , 2 AND 3 
'''
class Total:
    def __init__(self):
        # Initialize the total amounts to 0
        self.total1 = 0
        self.total2 = 0
        self.total3 = 0

    def calculate_total(self, item1, item4, item2, item3):
        # Calculate total for all items
        self.total1 = item1.print_price()  # Call print_price and get the total from item1 (Groceries)
        self.total4 = item4.print_price()  # Call print_price and get the total from item4 (Groceries)
        self.total2 = item2.print_price()  # Call print_price and get the total from item2 (Cosmetics)
        self.total3 = item3.print_price()  # Call print_price and get the total from item3 (Clothes)
        self.total=self.total1 + self.total4 + self.total2 + self.total3
    def print_total(self):
        # Print the total amount
        print(f'''
                ################# TOTAL = {self.total} Rs ###################
                ''')

# AddiNG ITEM INFO FOR THE ALL CATAGORY ITEMS
item1=GROCERIES(100,"Mung Dal")
item4=GROCERIES(3400,"WHEAT ")
item1.label()
item2=COSITEMS(600,"MAKE UP")
item3=CLOTHITEMS(1500,"FORMAL SHIRT")

# Create a Total object
final_total = Total()

# Calculate the total for all items
final_total.calculate_total(item1, item4, item2, item3)

# Print the total amount
final_total.print_total()




