class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaruant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restaruant_name + " is open now.")

'''Restaurant_1 = Restaurant('Hai_Di_Lao','hot_pot')
print(Restaurant_1.restaruant_name)
print(Restaurant_1.cuisine_type)
Restaurant_1.describe_restaurant()
Restaurant_1.open_restaurant()
'''

