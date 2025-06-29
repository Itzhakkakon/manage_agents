import mysql
import mysql.connector

config = {
    "user":"root",
    "host":"localhost",
    "database":"eagleeyedb",
    "port":3306}



def get_db_connection(_config=config) -> mysql.connector.connection:
    """
    Establishes a connection to the MySQL database using the provided configuration.
    :param _config: dict: Configuration dictionary containing database connection parameters.
    :return: mysql.connector.connection: A connection object to the MySQL database.
    """
    try:
        return mysql.connector.connect(**_config)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None