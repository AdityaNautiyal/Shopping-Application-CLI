prod = {}


def add_product():
    product_name = input("Enter Product Name: ")
    unit_price = int(input("Enter Unit Price: "))
    product = {product_name: unit_price}
    global prod
    prod.update(product)


def update_product():
    ProductName = input("Enter Product Name: ")
    global prod
    if ProductName in prod:
        UnitPrice = int(input("Enter New Price: "))
        prod[ProductName] = UnitPrice
        print("!! Product Updated !!")
    else:
        print("Product not available, Please add it to stock !!")


def remove_product():
    ProductName = input("Enter product Name: ")
    global prod
    if ProductName in prod:
        del prod[ProductName]
    else:
        print("Either Product is not in stock list or you misspelled")


def view_product():
    global prod
    print("Current items in the Stock are\n")
    print("{:<15} {}".format("Products", "Price"))
    for product, price in prod.items():
        print('{:<15} Rs{}'.format(product, price))


def admin():
    print("-"*70)
    print("   WELCOME TO ADMINISTRATION MODULE OF ONLINE RETAIL SHOPPING APP   ")
    print("-"*70)
    print("\n")

    while (True):
        print("-"*70, "\n")
        print("\t[1]. Add product in stock")
        print("\t[2]. Update product in stock")
        print("\t[3]. Remove product in stock")
        print("\t[4]. View product in stock")
        print("\t[5]. Sign Out\n")
        print("\n", '-'*70,"\n")
        print("\n")
        choice = input("Your Choice Here: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            remove_product()
        elif choice == '4':
            view_product()
        elif choice == '5':
            return False


# --------------------------------------------------------------------------
basket = {}
qty = {}


def addBasket():
    product_name = input("Enter Product Name: ")
    global prod
    global qty
    global basket

    if product_name in prod:
        basket[product_name] = prod[product_name]
    else:
        print("Either Product is not present in stock or you misspelled ")
    if product_name in basket:
        quantity = int(input("Enter No. of Units: "))
        qty[product_name] = quantity


def viewBasket():
    global basket
    print('{:<20} {:<5} {:<6} {:<7}'.format("Products", "unit", "Price", "Total"))
    gTotal = 0
    for product, price in basket.items():
        gTotal = (qty[product] * price) + gTotal
        print('{:<20} {:<5} {:<6} {:<7}'.format(product.title(), qty[product], price, qty[product] * price))

def searchBasket():
    product = input("Enter Product Name: ")
    if product in prod:
        print("Product is available")
    else:
        print("Product not Present in stock")


def removeBasket():
    ProductName = input("Enter product name: ")
    global basket
    if ProductName in basket:
        del basket[ProductName]
        del qty[ProductName]
    else:
        print("Product not present in basket")


def printInvoice():
    import datetime
    now = datetime.datetime.now()
    cdate = now.strftime('%d-%m-%Y')
    name = input("Please Enter Customer Name to be printed on invoice: ")
    print("\n\n")
    print("Name: ",name)
    print("Date: ",cdate)
    print("\n")
    print("-"*40)
    print("\n")
    global basket
    print('{:<20} {:<5} {:<6} {:<7}'.format("Products", "Unit", "Price", "Total"))
    print("\n")
    gTotal = 0
    for product, price in basket.items():
        gTotal = (qty[product] * price) + gTotal
        print('{:<20} {:<5} {:<6} {:<7}'.format(product.title(), qty[product], price, qty[product] * price))
    print(40 * '-')
    print("Grand Total = ", 'Rs {:<20}'.format(gTotal))
    print("-"*40)
    print()
    print("Thank You For Shopping!!")




def user():
    print("-"*70)
    print("    WELCOME TO USER MODULE OF ONLINE RETAIL SHOPPING APP   ")
    print("-"*70)
    print("\n")

    while (True):
        print("-"*70,"\n")
        print("\t[1]. View All product in stock")
        print("\t[2]. Add to shopping basket")
        print("\t[3]. View All product of basket")
        print("\t[4]. Search product in stock")
        print("\t[5]. Remove product from basket")
        print("\t[6]. Print Invoice")
        print("\t[7]. Sign Out\n")
        print("-"*70)
        print("\n")
        choice = input("Your Choice Here: ")
        if choice == '1':
            view_product()
        elif choice == '2':
            addBasket()
        elif choice == '3':
            viewBasket()
        elif choice == '4':
            searchBasket()
        elif choice == '5':
            removeBasket()
        elif choice == '6':
            printInvoice()
        elif choice == '7':
            return False



def main():
    input("Enter any key to start")
    admin()
    while(True):
        user()
        print("\n")
        print("This Program Has Been Successfully Executed")
        print("Developed by: Aditya Nautiyal")
        inp = input("Press Y to shop again and E to exit: ")
        if inp == 'Y':
            global basket
            global qty
            basket={}
            qty={}
            continue
        elif inp == 'E':
            return False


main()
