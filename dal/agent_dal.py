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

def add_agent(agent: tuple) -> bool:
    """
    Adds a new agent to the database.
    :param agent: dict: A dictionary containing agent details.
    :return: bool: True if the agent was added successfully, False otherwise.
    """
    add_agent_query = ("INSERT INTO `agents`("
                       "`code_name`,"
                       " `real_name`,"
                       " `location`,"
                       " `status`,"
                       " `missions_completed`)"
                       " VALUES (%s, %s, %s, %s, %s)")
    with get_db_connection() as conn:
        if conn.is_connected():
            with conn.cursor() as cmd:
                cmd.execute(add_agent_query, agent)
                conn.commit()
                return True
        else:
            print("Failed to connect to the database.")
            return False

if __name__ == "__main__":
    # Example usage
    print(get_all_agents())
    print(add_agent(("Agent001", "John Doe", "New York", "Active", 3)))
    print(add_agent(("Agent002", "Jane Smith", "Los Angeles", "Inactive", 2)))
    print(get_all_agents())
    print(add_agent(("Agent007", "James Bond", "London", "Active", 5)))
