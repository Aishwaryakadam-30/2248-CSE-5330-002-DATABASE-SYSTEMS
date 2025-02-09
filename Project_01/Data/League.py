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
        with open(r'path_to_your_csv_file\league.csv', 'r') as file:
            csv_reader = csv.reader(file)

            # Skipping the header row (if it exists)
            next(csv_reader)

            # Reading and inserting each row
            for row in csv_reader:
                if len(row) >= 3:  # Ensure the row has all required fields
                    (id, country_id, name) = row[:3]

                    # Executing the insert query
                    cursor.execute("""
                        INSERT INTO League (
                            id, country_id, name
                        ) 
                        VALUES (%s, %s, %s)
                    """, (id, country_id, name))

        # Commit the transaction to save all changes
        connection.commit()

except Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
