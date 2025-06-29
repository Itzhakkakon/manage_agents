from db_connection import get_db_connection

def get_all_agents() -> list[dict]:
    """
    Retrieves all agents from the database.
    :return: list: A list of dictionaries, each representing an agent.
    """
    get_all_query = "SELECT * FROM agents"
    with get_db_connection() as conn:
        if  conn.is_connected():
            with conn.cursor(dictionary=True) as cmd:
                cmd.execute(get_all_query)
                return cmd.fetchall()
        else:
            print("Failed to connect to the database.")
            exit(1)