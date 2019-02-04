# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Our Store!"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print(store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for st in stores:
        if st.name == store_name:
            return st
    else:
        return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    s = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes. \n")
    
    if s == "checkout":
        return False 
    for store in stores:
        if store.name == s:
            return get_store(s)
    else:
        print("No store with that name. Please try again.")
        s = input()
        



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    product = input("Please choose products(write 'back' to go back to stores): ")
    while not(product == 'back'):
        for p in picked_store.products:
            if product == p.name:
                cart.add_to_cart(p)
        else:
            product = input("and...")

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    store = pick_store()
    while not(store == False):
        pick_products(cart, store)
        store = pick_store()
    else:
        cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
