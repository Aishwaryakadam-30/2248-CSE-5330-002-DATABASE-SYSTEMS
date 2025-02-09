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
        with open(r'C:\Users\aishw\Downloads\Soccer-1 (1)\Soccerplayer_attributes.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 41:  # Make sure the row has all the necessary columns
                    (id, player_fifa_api_id, player_api_id, date, overall_rating, potential, preferred_foot, 
                     attacking_work_rate, defensive_work_rate, crossing, finishing, heading_accuracy, 
                     short_passing, volleys, dribbling, curve, free_kick_accuracy, long_passing, 
                     ball_control, acceleration, sprint_speed, agility, reactions, balance, shot_power, 
                     jumping, stamina, strength, long_shots, aggression, interceptions, positioning, 
                     vision, penalties, marking, standing_tackle, sliding_tackle, gk_diving, 
                     gk_handling, gk_kicking, gk_positioning, gk_reflexes) = row[:41]

                    # Executing the insert query
                    cursor.execute("""
                        INSERT INTO player_attributes (
                            id, player_fifa_api_id, player_api_id, date, overall_rating, potential, 
                            preferred_foot, attacking_work_rate, defensive_work_rate, crossing, 
                            finishing, heading_accuracy, short_passing, volleys, dribbling, curve, 
                            free_kick_accuracy, long_passing, ball_control, acceleration, sprint_speed, 
                            agility, reactions, balance, shot_power, jumping, stamina, strength, long_shots, 
                            aggression, interceptions, positioning, vision, penalties, marking, standing_tackle, 
                            sliding_tackle, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes
                        ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (id, player_fifa_api_id, player_api_id, date, overall_rating, potential, preferred_foot, 
                          attacking_work_rate, defensive_work_rate, crossing, finishing, heading_accuracy, 
                          short_passing, volleys, dribbling, curve, free_kick_accuracy, long_passing, 
                          ball_control, acceleration, sprint_speed, agility, reactions, balance, shot_power, 
                          jumping, stamina, strength, long_shots, aggression, interceptions, positioning, 
                          vision, penalties, marking, standing_tackle, sliding_tackle, gk_diving, 
                          gk_handling, gk_kicking, gk_positioning, gk_reflexes))

        # Commit the transaction
        connection.commit()

except Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
