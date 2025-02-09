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
        with open(r'patC:\Users\aishw\Downloads\Soccer-1 (1)\Soccer\match.csv', 'r') as file:
            csv_reader = csv.reader(file)

            # Skipping the header row (if it exists)
            next(csv_reader)

            # Reading and inserting each row
            for row in csv_reader:
                if len(row) >= 115:  # Ensure the row has all required fields
                    (id, country_id, league_id, season, stage, date, match_api_id, home_team_api_id, away_team_api_id, 
                    home_team_goal, away_team_goal, home_player_X1, home_player_X2, home_player_X3, home_player_X4, 
                    home_player_X5, home_player_X6, home_player_X7, home_player_X8, home_player_X9, home_player_X10, 
                    home_player_X11, away_player_X1, away_player_X2, away_player_X3, away_player_X4, away_player_X5, 
                    away_player_X6, away_player_X7, away_player_X8, away_player_X9, away_player_X10, away_player_X11, 
                    home_player_Y1, home_player_Y2, home_player_Y3, home_player_Y4, home_player_Y5, home_player_Y6, 
                    home_player_Y7, home_player_Y8, home_player_Y9, home_player_Y10, home_player_Y11, away_player_Y1, 
                    away_player_Y2, away_player_Y3, away_player_Y4, away_player_Y5, away_player_Y6, away_player_Y7, 
                    away_player_Y8, away_player_Y9, away_player_Y10, away_player_Y11, home_player_1, home_player_2, 
                    home_player_3, home_player_4, home_player_5, home_player_6, home_player_7, home_player_8, 
                    home_player_9, home_player_10, home_player_11, away_player_1, away_player_2, away_player_3, 
                    away_player_4, away_player_5, away_player_6, away_player_7, away_player_8, away_player_9, 
                    away_player_10, away_player_11, goal, shoton, shotoff, foulcommit, card, cross, corner, possession, 
                    B365H, B365D, B365A, BWH, BWD, BWA, IWH, IWD, IWA, LBH, LBD, LBA, PSH, PSD, PSA, WHH, WHD, WHA, 
                    SJH, SJD, SJA, VCH, VCD, VCA, GBH, GBD, GBA, BSH, BSD, BSA) = row[:115]

                    # Executing the insert query
                    cursor.execute("""
                        INSERT INTO Match (
                            id, country_id, league_id, season, stage, date, match_api_id, home_team_api_id, 
                            away_team_api_id, home_team_goal, away_team_goal, home_player_X1, home_player_X2, 
                            home_player_X3, home_player_X4, home_player_X5, home_player_X6, home_player_X7, 
                            home_player_X8, home_player_X9, home_player_X10, home_player_X11, away_player_X1, 
                            away_player_X2, away_player_X3, away_player_X4, away_player_X5, away_player_X6, 
                            away_player_X7, away_player_X8, away_player_X9, away_player_X10, away_player_X11, 
                            home_player_Y1, home_player_Y2, home_player_Y3, home_player_Y4, home_player_Y5, 
                            home_player_Y6, home_player_Y7, home_player_Y8, home_player_Y9, home_player_Y10, 
                            home_player_Y11, away_player_Y1, away_player_Y2, away_player_Y3, away_player_Y4, 
                            away_player_Y5, away_player_Y6, away_player_Y7, away_player_Y8, away_player_Y9, 
                            away_player_Y10, away_player_Y11, home_player_1, home_player_2, home_player_3, 
                            home_player_4, home_player_5, home_player_6, home_player_7, home_player_8, 
                            home_player_9, home_player_10, home_player_11, away_player_1, away_player_2, 
                            away_player_3, away_player_4, away_player_5, away_player_6, away_player_7, 
                            away_player_8, away_player_9, away_player_10, away_player_11, goal, shoton, 
                            shotoff, foulcommit, card, cross, corner, possession, B365H, B365D, B365A, BWH, BWD, 
                            BWA, IWH, IWD, IWA, LBH, LBD, LBA, PSH, PSD, PSA, WHH, WHD, WHA, SJH, SJD, SJA, 
                            VCH, VCD, VCA, GBH, GBD, GBA, BSH, BSD, BSA
                        ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (id, country_id, league_id, season, stage, date, match_api_id, home_team_api_id, away_team_api_id, 
                          home_team_goal, away_team_goal, home_player_X1, home_player_X2, home_player_X3, home_player_X4, 
                          home_player_X5, home_player_X6, home_player_X7, home_player_X8, home_player_X9, home_player_X10, 
                          home_player_X11, away_player_X1, away_player_X2, away_player_X3, away_player_X4, away_player_X5, 
                          away_player_X6, away_player_X7, away_player_X8, away_player_X9, away_player_X10, away_player_X11, 
                          home_player_Y1, home_player_Y2, home_player_Y3, home_player_Y4, home_player_Y5, home_player_Y6, 
                          home_player_Y7, home_player_Y8, home_player_Y9, home_player_Y10, home_player_Y11, away_player_Y1, 
                          away_player_Y2, away_player_Y3, away_player_Y4, away_player_Y5, away_player_Y6, away_player_Y7, 
                          away_player_Y8, away_player_Y9, away_player_Y10, away_player_Y11, home_player_1, home_player_2, 
                          home_player_3, home_player_4, home_player_5, home_player_6, home_player_7, home_player_8, 
                          home_player_9, home_player_10, home_player_11, away_player_1, away_player_2, away_player_3, 
                          away_player_4, away_player_5, away_player_6, away_player_7, away_player_8, away_player_9, 
                          away_player_10, away_player_11, goal, shoton, shotoff, foulcommit, card, cross, corner, 
                          possession, B365H, B365D, B365A, BWH, BWD, BWA, IWH, IWD, IWA, LBH, LBD, LBA, PSH, PSD, PSA, 
                          WHH, WHD, WHA, SJH, SJD, SJA, VCH, VCD, VCA, GBH, GBD, GBA, BSH, BSD, BSA))

        # Commit the transaction to save all changes
        connection.commit()

except Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
