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
        with open(r'C:\Users\aishw\Downloads\Soccer-1 (1)\Soccer\team_attributes.csv', 'r') as file:
            csv_reader = csv.reader(file)

            # Skipping the header row (if it exists)
            next(csv_reader)

            # Reading and inserting each row
            for row in csv_reader:
                if len(row) >= 25:  # Ensure the row has all required fields
                    (id, team_fifa_api_id, team_api_id, date, buildUpPlaySpeed, buildUpPlaySpeedClass, 
                     buildUpPlayDribbling, buildUpPlayDribblingClass, buildUpPlayPassing, 
                     buildUpPlayPassingClass, buildUpPlayPositioningClass, chanceCreationPassing, 
                     chanceCreationPassingClass, chanceCreationCrossing, chanceCreationCrossingClass, 
                     chanceCreationShooting, chanceCreationShootingClass, chanceCreationPositioningClass, 
                     defencePressure, defencePressureClass, defenceAggression, defenceAggressionClass, 
                     defenceTeamWidth, defenceTeamWidthClass, defenceDefenderLineClass) = row[:25]

                    # Executing the insert query
                    cursor.execute("""
                        INSERT INTO Team_Attributes (
                            id, team_fifa_api_id, team_api_id, date, buildUpPlaySpeed, buildUpPlaySpeedClass, 
                            buildUpPlayDribbling, buildUpPlayDribblingClass, buildUpPlayPassing, 
                            buildUpPlayPassingClass, buildUpPlayPositioningClass, chanceCreationPassing, 
                            chanceCreationPassingClass, chanceCreationCrossing, chanceCreationCrossingClass, 
                            chanceCreationShooting, chanceCreationShootingClass, chanceCreationPositioningClass, 
                            defencePressure, defencePressureClass, defenceAggression, defenceAggressionClass, 
                            defenceTeamWidth, defenceTeamWidthClass, defenceDefenderLineClass
                        ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (id, team_fifa_api_id, team_api_id, date, buildUpPlaySpeed, buildUpPlaySpeedClass, 
                          buildUpPlayDribbling, buildUpPlayDribblingClass, buildUpPlayPassing, 
                          buildUpPlayPassingClass, buildUpPlayPositioningClass, chanceCreationPassing, 
                          chanceCreationPassingClass, chanceCreationCrossing, chanceCreationCrossingClass, 
                          chanceCreationShooting, chanceCreationShootingClass, chanceCreationPositioningClass, 
                          defencePressure, defencePressureClass, defenceAggression, defenceAggressionClass, 
                          defenceTeamWidth, defenceTeamWidthClass, defenceDefenderLineClass))

        # Commit the transaction to save all changes
        connection.commit()

except Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if connection is connected:
        cursor.close()
        connection.close()
