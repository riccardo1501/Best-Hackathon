import openai
import json
# Import the Agent class from the agent module
from agent import Agent
from product import Product, get_products
from typing import List

# Define the API key as a global variable
API_KEY = "your_openai_api_key_here"  # Replace with your actual API key

def get_prompt(agent: Agent, products: List[Product]):
    prompt = f"""
You are a {agent.age}-year-old person looking to buy a powerbank on Amazon. You need it for {agent.use_case}. 
You’re {'' if agent.tech_savvy else 'not very ' }familiar with tech and {'do' if agent.tech_savvy else "don't " }understand the technical aspects. 
You {'' if agent.brand_conscious else "don't " }know about powerbank brands and you {'' if agent.brand_conscious else "don't " }care about the brand. 
You plan to use your powerbank to charge your {', '.join(agent.devices)}.

Now, you are browsing through a list of powerbanks on Amazon. Consider the options available based on your preferences, and choose the one you would purchase. 
Explain why you would select it, taking into account factors such as charging speed, compatibility with your devices, and overall value.

Here are some options you are considering:

"""

    # Add the product strings (using the __str__ method for each product)
    for product in products:
        prompt += f"\n{product}\n"  # Each product's detailed string representation

    return prompt


def call_gpt35_api(prompt: str) -> dict:
    # Set the OpenAI API key using the global variable
    openai.api_key = API_KEY
    
    try:
        # Make the API call to GPT-3.5
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3.5 engine
            prompt=prompt,
            max_tokens=100,  # Adjust max tokens as needed
            n=1,  # Number of completions to generate
            stop=None,  # Stop sequences (if any)
            temperature=0.7  # Controls randomness
        )
        
        # Return the response as a JSON object
        return response

    except Exception as e:
        print(f"Error calling GPT-3.5 API: {e}")
        return {"error": str(e)}

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
    prompt = get_prompt(agent, products)
    print(prompt)
    #response_json = call_gpt35_api(prompt)

    # Print the response JSON in a pretty format
    #print(json.dumps(response_json, indent=2))

