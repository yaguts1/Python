from restaurant import Restaurant

# Make a class to represent the menu items
class Item_menu(Restaurant):
    def __init__(self,item_name,item_price,item_description,my_unpickled_restaurant_object):
        self.item_name =  item_name
        self.item_price = item_price
        self.item_description = item_description
        self.restaurant = my_unpickled_restaurant_object
    def display2(self):  
        print("Restaurant: %s \nDistance: %s \nReview: %s \nLink: %s \nDelivery expected time: %s \nDelivery fee: %s \nFood category: %s \nItem name: %s \nItem price: %s \nItem description: %s \nRestaurant name: %s" % (self.restaurant.name.decode(), self.restaurant.distance,self.restaurant.review, self.restaurant.link, self.restaurant.delivery_time, self.restaurant.delivery_fee,self.restaurant.food_category,self.item_name.decode(),self.item_price,self.item_description))
