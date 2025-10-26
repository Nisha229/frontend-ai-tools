from typing import List, Optional
from pydantic import BaseModel, Field

class ai_summarizer_generator_options(BaseModel):
    topic: str 
    
class ai_summarizer_generator_request(BaseModel):
    strategy: str
    model: str 
    options: ai_summarizer_generator_options

class ai_summarizer_generator_response(BaseModel):
    ai_summarizer: str
