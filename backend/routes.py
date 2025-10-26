import logging
import traceback
from fastapi import APIRouter, HTTPException

# Import schemas
from models.tweet_idea_generator_schema import (
    tweet_ideas_generator_request,
    tweet_ideas_generator_response,
    TweetIdea,
)

from models.ai_summarizer_schema import (
    ai_summarizer_generator_request,
    ai_summarizer_generator_response,
)

from models.parapherising_schema import (
    parapherising_generator_request,
    parapherising_generator_response,
)

from models.blog_post_generator_schema import (
    blog_post_generator_request,
    blog_post_generator_response,
)

from models.social_media_bio_generator_schema import (
    social_media_bio_generator_request,
    social_media_bio_generator_response,
)

from generic_tool_generator import GenericToolGenerator

router = APIRouter()

# 1. Tweet Ideas Generator
tweet_tool = GenericToolGenerator(
    llm_name="gemini",
    prompt_dir="prompts/tweets-generator",
    prompt_file="gemini.txt.j2"
)

@router.post("/generate-tweet-ideas", response_model=tweet_ideas_generator_response)
async def generate_tweet_ideas(request: tweet_ideas_generator_request):
    try:
        options_dict = request.options.dict() if hasattr(request.options, "dict") else dict(request.options)
        output_text = tweet_tool.run(options_dict, request.model)

        tweet_lines = [
            line.strip("-•* ").strip()
            for line in output_text.strip().split("\n")
            if line.strip()
        ]
        tweet_ideas = [TweetIdea(text=tweet) for tweet in tweet_lines]
        return tweet_ideas_generator_response(tweet_ideas=tweet_ideas)

    except Exception as e:
        logging.error("Error generating tweet ideas:\n" + traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to generate tweet ideas.")

# 2. AI Summarizer
summarizer_tool = GenericToolGenerator(
    llm_name="gemini",
    prompt_dir="prompts/ai-summarizer",
    prompt_file="gemini.txt.j2"
)

@router.post("/ai-summarizer", response_model=ai_summarizer_generator_response)
async def ai_summarizer(request: ai_summarizer_generator_request):
    try:
        options_dict = request.options.dict() if hasattr(request.options, "dict") else dict(request.options)
        output_text = summarizer_tool.run(options_dict, request.model)
        return ai_summarizer_generator_response(ai_summarizer=output_text)

    except Exception as e:
        logging.error("Error generating summarizing text:\n" + traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to generate summarizer text.")

# 3. Paraphrasing Tool
paraphrasing_tool = GenericToolGenerator(
    llm_name="gemini",
    prompt_dir="prompts/parapherising",
    prompt_file="gemini.txt.j2"
)

@router.post("/paraphrase", response_model=parapherising_generator_response)
async def parapherising(request: parapherising_generator_request):
    try:
        options_dict = request.options.dict() if hasattr(request.options, "dict") else dict(request.options)
        output_text = paraphrasing_tool.run(options_dict, request.model)
        return parapherising_generator_response(output=output_text)

    except Exception as e:
        logging.error("Error generating paraphrased text:\n" + traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to generate paraphrased text.")

# 4. Blog Post Generator
blog_tool = GenericToolGenerator(
    llm_name="gemini",
    prompt_dir="prompts/blog_post_generator",
    prompt_file="gemini.txt.j2"
)

@router.post("/blog-post-generator", response_model=blog_post_generator_response)
async def blog_post_generator(request: blog_post_generator_request):
    try:
        options_dict = request.options.dict() if hasattr(request.options, "dict") else dict(request.options)
        output_text = blog_tool.run(options_dict, request.model)
        return blog_post_generator_response(output=output_text)

    except Exception as e:
        logging.error("Error generating blog post:\n" + traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to generate blog post.")

# 5. Social Media Bio Generator
bio_tool = GenericToolGenerator(
    llm_name="gemini",
    prompt_dir="prompts/social_media_bio_generator",
    prompt_file="gemini.txt.j2"
)

@router.post("/social-media-bio-generator", response_model=social_media_bio_generator_response)
async def social_media_bio_generator(request: social_media_bio_generator_request):
    try:
        options_dict = request.options.dict() if hasattr(request.options, "dict") else dict(request.options)
        output_text = bio_tool.run(options_dict, request.model)
        return social_media_bio_generator_response(output=output_text)

    except Exception as e:
        logging.error("Error generating social bio:\n" + traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to generate social bio.")
