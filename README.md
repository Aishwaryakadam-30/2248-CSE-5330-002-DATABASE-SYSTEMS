# 2248-CSE-5330-002-DATABASE-SYSTEMS

This repository contains SQL scripts and Python scripts for managing a soccer database in MySQL. The scripts handle inserting data from CSV files, enforcing foreign key constraints, and resolving common database errors.

## Project Structure

```
GithubReposterUIOY/
│-- scripts/
│   ├── Country.py
│   ├── League.py
│   ├── Match.py
│   ├── Player.py
│   ├── Player_Attributes.py
│   ├── Team.py
│   ├── Team_Attributes.py
│-- sql/
│   ├── Create_table.sql
│-- logs/
│   ├── Question_4_Spool.log
│   ├── Question_5_Spool.log
│   ├── Question_6_Spool.log
│-- docs/
│   ├── Schema_Diagram.pdf
│-- .gitignore
│-- README.md
```

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/GithubReposterUIOY.git
   ```
2. Navigate to the directory:
   ```sh
   cd GithubReposterUIOY
   ```
3. Install required dependencies:
   ```sh
   pip install mysql-connector-python
   ```

## Database Configuration
Modify the `db_config` dictionary in each Python file to match your database credentials:

```python
# Database configuration
 db_config = {
    'host': 'your_host',
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password'
 }
```

## Usage
- **SQL Schema:** The `Create_table.sql` file contains the schema for setting up the database.
- **Python Scripts:** Each script reads a CSV file and inserts data into the MySQL tables.
- **Logs:** Error logs from previous database operations are stored in the `logs/` directory.

Example execution:
```sh
python scripts/Country.py
```

Ensure the corresponding CSV file path is correct in the script before execution.

## License
This project is open-source and available for personal or educational use.


