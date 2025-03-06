#Define the menu of resturant
menu = {
    'Coffee':90,
    'Maggi':50,
    'Pizza':100,
    'Burger':80,
    'Pasta':70,
    'Salad':40,
}

#Greet
print("Welcome to SM Resturant")
print("Coffee: Rs90\n Maggi: Rs50\n Pizza: Rs100\n Burger: Rs80\n Pasta: Rs70\n Salad: Rs40")

#Make a variable 
#90 + 50 = 140
order_total = 0

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total +=menu[item_1] #0 + 90 = 90
    print(f"Your item{item_1} has been added your order") #f means forwarded string

else:
    print(f"Ordered item{item_1} is not avaialable yet")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item{item_2} has been added to order")
    else:
        print(f"Ordered item{item_2} is not avaialable")

print(f"The total amount of item to pay is{order_total}")                     