import mysql.connector
from faker import Faker

Faker.seed(30987)
fake = Faker()
con = mysql.connector.connect(host='localhost', database='testing', user='test', password='test')

if con.is_connected():
    cursor = con.cursor()
    for i in range(100):
        lname = fake.last_name()
        fname = fake.first_name()
        bdate = fake.date_between(start_date='-60y', end_date='-10y')
        phone = fake.phone_number()
        addr = fake.address()
        print(lname, fname, bdate, phone, addr)
        cursor.execute('INSERT INTO customers (last_name,first_name,birthdate,phone,address) \
                       VALUES ("%s","%s","%s","%s","%s");' % (lname, fname, bdate, phone, addr))
    con.commit()
else:
    print("problem")
