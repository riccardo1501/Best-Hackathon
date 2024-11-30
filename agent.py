from typing import List

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
    pass
