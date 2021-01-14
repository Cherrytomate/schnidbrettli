from woocommerce import API
import os

class Customer:
    email = None
    surname = None
    lastname = None
    phone = None
    address = None
    city = None
    state = None
    postcode = None

    def __init__(self, email, surname, lastname, phone, address, city, state, postcode):
        self.email = email
        self.surname = surname
        self.lastname = lastname
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.postcode = postcode




def get_customer_data():

        wcapi = API(
            url=os.getenv("URL"),
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_SECRET"),
            version="wc/v3"
        )

        r = wcapi.get("orders")
        print(r.json())
        json_array = r.json()
        store_list = []
        for item in json_array:
            if item['status'] == 'completed':
                email = item['billing']['email']
                surname = item['billing']['first_name']
                lastname = item['billing']['last_name']
                phone = item['billing']['phone']
                address = item['billing']['address_1'] + " " + item['billing']['address_2']
                city = item['billing']['city']
                postcode = item['billing']['postcode']
                state = item['billing']['state']

        customer = Customer(email, surname, lastname, phone, address, city, state, postcode)
        print(customer.surname,customer.lastname,customer.phone,customer.address,customer.state,customer.city
              ,customer.postcode)
        return customer




        #with open("file.txt", "w") as output:
        #output.write(str(item))
        #email_handler(email, surname)