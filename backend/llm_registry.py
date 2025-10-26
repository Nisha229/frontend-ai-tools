from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import ChatOpenAI

def get_Gemini_llm(model_name, api_key):
    return ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)

LLM_LOADERS = {
    "gemini": get_Gemini_llm
}