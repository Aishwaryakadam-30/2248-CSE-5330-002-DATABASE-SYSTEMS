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
        with open(r'pC:\Users\aishw\Downloads\Soccer-1 (1)\Soccer\team.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 5:  # Ensure the row has all required columns
                    id, team_api_id, team_fifa_api_id, team_long_name, team_short_name = row[0], row[1], row[2], row[3], row[4]

                    # Executing the insert query
                    cursor.execute("""
                        INSERT INTO Team (id, team_api_id, team_fifa_api_id, team_long_name, team_short_name) 
                        VALUES (%s, %s, %s, %s, %s)
                    """, (id, team_api_id, team_fifa_api_id, team_long_name, team_short_name))

        # Commit the transaction
        connection.commit()

except Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
