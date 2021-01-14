from customer.email_manager import *
from customer.database_manager import *
from customer.customer_manager import *
import os

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_DATABASE = os.getenv("DATABASE_DATABASE")


def main():


    database_manager = DatabaseManager(DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_DATABASE)
    customer = get_customer_data()
    database_manager.insert_customer(customer)
    list = database_manager.check_review_sate()
    for customer in list:
        review_handler(customer[0],customer[1])

if __name__ == '__main__':
    main()
