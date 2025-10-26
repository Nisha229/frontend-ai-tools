from typing import List, Optional
from pydantic import BaseModel, Field

class social_media_bio_generator_options(BaseModel):
    platform:str = Field(..., example="Instagram")
    profile_type:str = Field(..., example="Personal")
    interests: List[str] = Field(..., example=["Traveling", "Photography", "Cooking"])
    tone:str 
    language:str 
    


class  social_media_bio_generator_request(BaseModel):
    strategy: str
    model: str 
    options:  social_media_bio_generator_options

class  social_media_bio_generator_response(BaseModel):
    output: str
