# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Shop It!"  # Give your site a name

def welcome():
	print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
	"""
	prints the list of stores in a nice readable format.
	"""
	# your code goes here!
	for store in stores:
	  print("- %s" % store.name)

def get_store(user_input):
	"""
	receives a name for a store, and returns the store object with that name.
	"""
	# your code goes here!
	for store in stores:
		if user_input == store.name.lower():
			return store
	return False

def pick_store(cart):
	"""
	prints list of stores and prompts user to pick a store.
	"""
	# your code goes here!
	user_input = input('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes\n').lower()
	if user_input == "checkout":
		cart.checkout()
	elif get_store(user_input) == False:
		print ("Sorry. No store with that name. Please try again.")
	else:
		store_object = get_store(user_input)
		pick_products(cart, store_object)

def pick_products(cart, picked_store):
	"""
	prints list of products and prompts user to add products to cart.
	"""
	# your code goes here!
	picked_store.print_products()
	print("Pick a Product to add to cart or type 'back'.")
	while True:
		productinput=input().lower()
		if productinput == "back":
			break
		else:
			for product in picked_store.products:
				if productinput == product.name.lower():
					cart.add_to_cart(product)	
	pick_store(cart)


def shop():
	"""
	The main shopping functionality
	"""
	cart = Cart()
	print_stores()
	pick_store(cart)
	# your code goes here!

def thank_you():
	print("Thank you for shopping with us at %s" % site_name)
