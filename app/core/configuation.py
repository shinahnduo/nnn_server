import os
import yaml


def load_config():
    env = os.getenv("APP_ENV", "local")  # 기본값 local
    print(env)
    config_path = f"./app/core/config/{env}.yaml"

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config
