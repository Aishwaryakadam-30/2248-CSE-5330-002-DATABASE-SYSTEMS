import mysql.connector
import csv
from mysql.connector import Error

# Database configuration
db_config = {
    'host': 'academicmysql.mysql.database.azure.com',
    'database': 'axk9035',
    'user': 'axk9035',
    'password': 'Aishu@325530'
}

try:
    # Establishing the connection
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        cursor = connection.cursor()

        # Opening the CSV file
        with open(r'paC:\Users\aishw\Downloads\Soccer-1 (1)\Soccer\country.csv', 'r') as file:
            csv_reader = csv.reader(file)

            # Skipping the header row (if it exists)
            next(csv_reader)

            # Reading and inserting each row
            for row in csv_reader:
                if len(row) >= 2:  # Ensure the row has all required fields
                    (id, name) = row[:2]

                    # Executing the insert query
                    cursor.execute("""
                        INSERT INTO Country (
                            id, name
                        ) 
                        VALUES (%s, %s)
                    """, (id, name))

        # Commit the transaction to save all changes
        connection.commit()

except Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
