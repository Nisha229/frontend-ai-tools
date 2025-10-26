from typing import List, Optional
from pydantic import BaseModel, Field

class tweet_ideas_generator_options(BaseModel):
    topic: str 
    hashtags_enabled: Optional[bool] = Field(False, description="Whether to include hashtags in the output.")
    create_thread: Optional[bool] = Field(False, description="Whether to structure the output as a thread.")
    tone: Optional[str] = Field(None, description="Writing tone and style (e.g., conversational, formal, default)")
    language: Optional[str] = Field("en", description="Language for blog output, e.g., 'English (US)'")
    creativity_level: Optional[str] = Field(None, description="Creativity slider (low, medium, high)")
    pov: Optional[str] = Field(None, description="Point of view (1st person, 3rd person, etc.)")
    target_audience: Optional[str] = Field(None, description="Target audience for the blog post")
    keyword: Optional[str] = Field(None, description="Add Additional keyword")
    additional_instructions: Optional[str] = Field(None, description="Any extra notes or requirements")

class TweetIdea(BaseModel):
    text: str

class tweet_ideas_generator_request(BaseModel):
    strategy: str
    model: str 
    options: tweet_ideas_generator_options

class tweet_ideas_generator_response(BaseModel):
    tweet_ideas: List[TweetIdea] 
