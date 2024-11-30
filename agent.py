from typing import List
import random
import numpy as np

class Agent:
    def __init__(self, 
                 age: int, 
                 behavior: str, 
                 use_case: str, 
                 tech_savvy: bool, 
                 brand_conscious: bool, 
                 devices: List[str]):
        self.age: int = age  # int
        self.behavior: str = behavior  # str
        self.use_case: str = use_case  # str
        self.tech_savvy: bool = tech_savvy  # bool
        self.brand_conscious: bool = brand_conscious  # bool
        self.devices: List[str] = devices  # list of strings


def create_agents():
    age = random.randint(18, 65)
    behaviour = np.random.choice(["Impulsive behavior: refers to quick, often emotional decisions without much thought or evaluation. Impulsive buyers are driven by immediate desires rather than rational planning", "Reflective behavior: refers to thoughtful, deliberate purchasing decisions based on careful evaluation. Reflective buyers take their time, compare options, and focus on long-term value"], p=[0.6, 0.4])
    use_case = np.random.choice(["work", "travel", "personal use"])
    tech_savvy = np.random.choice([True, False], p=[0.6, 0.4])
    brand_conscious = np.random.choice([True, False], p=[0.6, 0.4])
    devices = np.random.choice(['smartphone', 'PC', 'tablet', 'altri'], p=[0.5, 0.3, 0.1, 0.1])

    agent = Agent(
        age=age,
        behavior=behaviour,
        use_case=use_case,
        tech_savvy=tech_savvy,
        brand_conscious=brand_conscious,
        devices=devices
    )

    return agent

if __name__ == "__main__":
    create_agents()