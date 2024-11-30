from api import *
from agent import *
from tqdm import tqdm

def get_agents_response(n):
    result = {}

    for i in tqdm(range(n)):
        agent = create_agents()
        products = get_products("./products.json")
        system, user = get_prompt(agent, products)
        product_number, reason_to_buy = call_gpt(system, user)

        agent_name = "Agent_{}".format(i)
        result[agent_name] = {"product_number": product_number, "reason_to_buy": reason_to_buy}

    
    return result


def run_simulation(n_agents):
    result = get_agents_response(n_agents)
    summary_purchase = {"product_1": 0, "product_2": 0, "product_3": 0, "product_4": 0, "product_5": 0}

    for agent in result:
        if result[agent]["product_number"] == 1:
            summary_purchase["product_1"] += 1
        elif result[agent]["product_number"] == 2:
            summary_purchase["product_2"] += 1
        elif result[agent]["product_number"] == 3:
            summary_purchase["product_3"] += 1
        elif result[agent]["product_number"] == 4:
            summary_purchase["product_4"] += 1
        else:
            summary_purchase["product_5"] += 1

    print(summary_purchase)

    return result


if __name__ == "__main__":
    run_simulation(20)