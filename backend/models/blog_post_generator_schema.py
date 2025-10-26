from typing import List, Optional
from pydantic import BaseModel, Field

class blog_post_generator_options(BaseModel):
    topic: str 
    keyboard: str
    


class  blog_post_generator_request(BaseModel):
    strategy: str
    model: str 
    options:  blog_post_generator_options

class  blog_post_generator_response(BaseModel):
    output: str
