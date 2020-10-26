number_of_copies = int(input("number of copies:")) 
cover_price_of_book = 24.95 
discount_proportion = 0.4 
first_loss = (cover_price_of_book * discount_proportion)
total_shipping_cost = ((number_of_copies - 1) * (0.75) + (1 * 3))
total_loss = first_loss + total_shipping_cost 
print("total loss: {:.2f}".format(total_loss))