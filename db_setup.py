import pymysql
from settings import *

conn = pymysql.connect(host=host, user=user, password=password)
print(conn)

cur = conn.cursor()

cur.execute(f'''DROP DATABASE IF EXISTS {database}''')
cur.execute(f'''CREATE DATABASE {database}''')

cur.execute(f'''USE {database}''')

tables = ['user', 'transaction', 'transaction_details']

cur.execute(
    f'''
    CREATE TABLE user (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        phone_number CHAR(13) NOT NULL
    )
    '''
)

conn.close()
