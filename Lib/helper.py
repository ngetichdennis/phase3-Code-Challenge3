from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review
def add_customer():
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    try:
        new_customer = Customer.create(first_name, last_name)
        print(f"Customer added successfully:{new_customer}")
        
    except Exception as exc:
        print("Error adding the customer", exc)
    
def add_restaurant():
    name = input("Enter the restaurant's name: ")
    price = input("Enter the restaurant's price: ")
    try:
        new_restaurant = Restaurant.create(name, price)
        print(f'Restaurant added successfully: {new_restaurant}')
    except Exception as exc:
        print("Error creating restaurant: ", exc)

def add_review():
    customer_id = int(input("Enter customer ID: "))
    restaurant_id = int(input("Enter restaurant ID: "))
    star_rating = int(input("Enter star rating (1-5): "))
    try:
        new_review = Review(customer_id, restaurant_id, star_rating)
        print(f"Review added successfully:{new_review}")
        
    except Exception as exc:
        print("Error adding review: ", exc)

def list_all_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(f"{customer.id}: {customer.full_name()}")

def list_all_restaurants():
    restaurants = Restaurant.get_all()
    for restaurant in restaurants:
        print(f"{restaurant.id}: {restaurant.name} ({restaurant.price} stars)")

def list_all_reviews():
    reviews = Review.get_all()
    for review in reviews:
        #fetch customer and restaurant objects
        customer=review.customer()
        restaurant=review.restaurant()
        print(f"Review for {restaurant.name} by  {customer.full_name()}: {review.star_rating} stars")

