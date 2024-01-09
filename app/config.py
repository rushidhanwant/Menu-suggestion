import os


class Config:
    root_dir = os.path.dirname(os.path.dirname((__file__)))
    env_path = os.path.join(root_dir, ".env")


config = Config()
