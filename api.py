import openai

# Initialize the OpenAI client and pass the API key directly
client = openai.OpenAI(api_key="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")

import json
# Import the Agent class from the agent module
from agent import Agent
from product import Product, get_products
from typing import List

def get_prompt(agent: Agent, products: List[Product]):
    system_prompt = f"""
You are a {agent.age}-year-old person looking to buy a powerbank on Amazon. You need it for {agent.use_case}. 
You’re {'' if agent.tech_savvy else 'not very ' }familiar with tech and {'do' if agent.tech_savvy else "don't " }understand the technical aspects. 
You {'' if agent.brand_conscious else "don't " }know about powerbank brands and you {'' if agent.brand_conscious else "don't " }care about the brand. 
You plan to use your powerbank to charge your {', '.join(agent.devices)}."""

    user_prompt = f"""Now, you are browsing through a list of powerbanks on Amazon. Consider the options available based on your preferences, and choose the one you would purchase. 
Explain why you would select it, taking into account factors such as charging speed, compatibility with your devices, and overall value.

Here are some options you are considering:"""

    # Add the product strings (using the __str__ method for each product)
    i = 1
    for product in products:
        user_prompt += f"i.\n{product}\n"  # Each product's detailed string representation
        i += 1

    return system_prompt, user_prompt

from pydantic import BaseModel
class Purchase(BaseModel):
    product_number: int
    reason_to_buy: str


def call_gpt(system_prompt: str, user_prompt: str) -> tuple: 
    completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    response_format=Purchase,
    temperature=0.5,
)
    purchase = completion.choices[0].message.parsed
    return purchase.product_number, purchase.reason_to_buy

# Example usage
if __name__ == "__main__":
    agent = Agent(
    age=30,
    behavior="",
    use_case="work",
    tech_savvy=True,
    brand_conscious=False,
    devices=["mobile", "laptop"]
)   
    products = get_products("./products.json")
    system_prompt, user_prompt = get_prompt(agent, products)
    product_number, reason_to_buy = call_gpt(system_prompt, user_prompt)
    print(product_number, reason_to_buy)

    # Print the response JSON in a pretty format
    #print(json.dumps(response_json, indent=2))

