#Create class
#First I need to create a class for restaurant
# This is called a constructor. It is responsible to give variables to the object while it creates it
class Restaurant():

    def __init__(self,name,distance,review,link,delivery_time,delivery_fee,food_category):
        self.name =  name
        self.distance = distance
        self.review = review
        self.link = link
        self.delivery_time = delivery_time
        self.delivery_fee = delivery_fee
        self.food_category = food_category
    def display(self):  
        print("Restaurant: %s \nDistance: %s \nReview: %s \nLink: %s \nDelivery expected time: %s \nDelivery fee: %s \nFood category: %s" % (self.name, self.distance,self.review, self.link, self.delivery_time, self.delivery_fee,self.food_category))