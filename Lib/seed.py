from models.__init__ import CONN, CURSOR
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review
def seed_database():
    Customer.drop_table()
    Restaurant.drop_table()
    Review.drop_table()
    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()
    #seed customer data
    Customer.create("Alice", "Smith"),
    Customer.create("Bob", "Johnson"),
    Customer.create("Charlie", "Brown"),
    Customer.create("Diana", "Wilson")

    # Seed restaurants
    Restaurant.create("Restaurant A", 3),
    Restaurant.create("Restaurant B", 4),
    Restaurant.create("Restaurant C", 5)
    # Seed reviews(Customer ID, Restaurant ID, Star Rating)
    Review.create(1, 1, 4),  
    Review.create   (1, 2, 5),
    Review.create   (2, 2, 3),
    Review.create   (2, 3, 4),
    Review.create   (3, 1, 5),
    Review.create  (3, 3, 4),
    Review.create  (4, 2, 3)

seed_database()
print("database successfully seeded")  
