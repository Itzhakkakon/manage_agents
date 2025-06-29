from models.agent import AgentStatus
from dal.agent_dal import get_all_agents, add_agent
import dal.agent_dal
from models.agent import agent as Agent

def main():
    agents =[
        ("agent1","John Doe","New York",'active',5),
        ("agent2","Jane Smith","Los Angeles",'INACTIVE',3),
        ("agent3","Alice Johnson","Chicago",'SUSPENDED',2)
    ]
    for agent in agents:
        if add_agent(agent):
            print(f"Added agent: {agent}")
        else:
            print(f"Failed to add agent: {agent}")


    print("All agents in the database:")
    for agent in get_all_agents():
        agent = Agent(**agent)  # Convert dict to Agent object
        print(agent)
if __name__ == "__main__":
    main()
    # print("All agents in the database:")
    # for agent in get_all_agents():
    #     print(agent)