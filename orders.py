import mysql.connector
from faker import Faker
import random
import decimal

Faker.seed(30987)
fake = Faker()
con = mysql.connector.connect(host='localhost', database='testing', user='test', password='test')

if con.is_connected():
    cursor = con.cursor()
    for i in range(3000):
        cid = random.randint(1, 100)
        price = float(decimal.Decimal(random.randrange(1100, 200000))/100)

        print(cid, price)
        cursor.execute('INSERT INTO orders (customer_id, price) \
                       VALUES ("%i","%f");' % (cid, price))
    con.commit()
else:
    print("problem")
