import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(variable_name: str):
    if variable_name not in os.environ:
        raise ValueError(f"Variable {variable_name} not found in environment")
    return os.getenv(variable_name)


DB_HOST = get_env_variable("DB_HOST")
DB_USERNAME = get_env_variable("DB_USERNAME")
DB_PASSWORD = get_env_variable("DB_PASSWORD")
DB_NAME = get_env_variable("DB_NAME")
