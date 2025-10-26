from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

def get_env(prompt_folder: str):
    prompt_path = Path(prompt_folder)
    env = Environment(
        loader=FileSystemLoader(str(prompt_path)),
        autoescape=select_autoescape(disabled_extensions=('txt', 'j2'))
    )
    return env

def load_prompt(prompt_folder: str, template_name: str, variables: dict) -> str:
    try:
        env = get_env(prompt_folder)
        template = env.get_template(template_name)
        return template.render(**variables).strip()
    except Exception as e:
        raise ValueError(f"Error loading prompt from {prompt_folder}/{template_name}: {e}")
