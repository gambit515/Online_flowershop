import mysql.connector

import pymysql

from Config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected..")
    print('#' * 20)
    try:
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE Account" \
                                 "(IdAc INT(10) NOT NULL AUTO_INCREMENT," \
                                 "Name VARCHAR(15) NOT NULL," \
                                 "SName VARCHAR(15) NOT NULL," \
                                 "TName VARCHAR(15) NOT NULL," \
                                 "Email VARCHAR(50) NOT NULL," \
                                 "PRIMARY KEY (IdAc))" \
                                 "CHARACTER SET=cp866;"
            cursor.execute(create_table_query)
            print("Table created successfully")
    except Exception as ex:
        print("команда говно")
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused..")
    print(ex)


