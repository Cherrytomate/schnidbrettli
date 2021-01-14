import logging
import sys
import mariadb

logger = logging.getLogger(__name__)


class DatabaseManager:

    _db_connection = None

    def __init__(self, user, password, host, database, port=3306):
        try:
            self._db_connection = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def __del__(self):
        self._db_connection.close()

    def insert_customer(self, customer):
        cursor = self._db_connection.cursor()
        try:
            cursor.execute("INSERT INTO customer_data (customer_email, customer_surname, customer_lastname, customer_phone, customer_adress,customer_state,	customer_city,customer_postcode, review_sent) VALUES (?,?, ?, ?, ?, ?,?,?,?)",
                           (customer.email, customer.surname, customer.lastname, customer.phone, customer.address, customer.state, customer.city
                            ,customer.postcode,1))
        except mariadb.Error as e:
            print(f"Error: {e}")

        self._db_connection.commit()
        return cursor.lastrowid



    def check_review_sate(self):
        cursor = self._db_connection.cursor()
        cursor.execute("SELECT customer_email,customer_surname from customer_data WHERE review_sent = (?)", (True,))
        list = cursor.fetchall()
        print(list)
        return list



