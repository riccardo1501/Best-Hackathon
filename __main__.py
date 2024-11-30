from api import *
from agent import *

def get_agents_response(n):
    result = {}

    for i in range(n):
        agent = create_agents()
        products = get_products("./products.json")
        prompt = get_prompt(agent, products)
        product_number, reason_to_buy = call_gpt35_api(prompt)

        agent_name = "{}agent".format(i)
        result[agent_name] = {"product_number": product_number, "reason_to_buy": reason_to_buy}

    
    return result