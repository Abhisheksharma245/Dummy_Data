import pymysql
import random
from faker import Faker
from settings import *


fake = Faker()

num_records = 400

conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()

for i in range(num_records):
    name = fake.name()
    email = fake.email()
    password = fake.password()
    phone = '+91' + str(random.randint(6000000000, 9999999999))

    cur.execute(
        f'''
        INSERT INTO user (name, email, password, phone_number)
        VALUES ('{name}', '{email}', '{password}', '{phone}')
        '''
    )
else:
    conn.commit()

conn.close()



