import yaml


def get_yaml(filepath: str):
    with open(file=filepath, encoding='utf-8') as f:
        return yaml.safe_load(f.read())
