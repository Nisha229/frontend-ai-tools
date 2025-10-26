from langchain.prompts import PromptTemplate
import re
from typing import Dict, Any
from langchain_core.language_models import BaseLanguageModel
from llm_registry import LLM_LOADERS
from prompts.template_loader import load_prompt
from config import settings

class GenericToolGenerator:
    def __init__(self, llm_name: str, prompt_dir: str, prompt_file: str):
        self.llm_name = llm_name.capitalize()
        self.api_key = getattr(settings, f"{llm_name.capitalize()}_api_key")
        self.llm_name = llm_name
        self.prompt_dir = prompt_dir
        self.prompt_file = prompt_file or f"{prompt_file}.txt.j2"
        self._llm_cache = {}

        print(llm_name)
    def run(self, options: Dict[str, Any], model_name: str) -> list[str]:
        # Load prompt from file
        if not isinstance(options, dict):
            options = options.dict()
        prompt_str = load_prompt(self.prompt_dir, self.prompt_file, options)

        # Format prompt using LangChain's PromptTemplate
        prompt_template = PromptTemplate(
            input_variables=list(options),
            template=prompt_str
        )

        # Load LLM instance
        if model_name not in self._llm_cache:
            llm_loader = LLM_LOADERS.get(self.llm_name)
            if not llm_loader:
                raise ValueError(f"Unsupported LLM: {self.llm_name}")
            self._llm_cache[model_name] = llm_loader(model_name, self.api_key)

        llm: BaseLanguageModel = self._llm_cache[model_name]

    # Send formatted prompt to LLM
        response = llm.invoke(prompt_str)
        result = response.content
        return result