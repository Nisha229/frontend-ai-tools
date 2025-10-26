from typing import List, Optional
from pydantic import BaseModel, Field

class parapherising_generator_options(BaseModel):
    input: str 
    


class  parapherising_generator_request(BaseModel):
    strategy: str
    model: str 
    options:  parapherising_generator_options

class  parapherising_generator_response(BaseModel):
    output: str
