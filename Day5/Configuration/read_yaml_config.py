import yaml

from pathlib import Path

config_file_path = Path("config.yaml")
#print(config_file_path)

with config_file_path.open(encoding="utf-8") as config_file:
    config=yaml.load(config_file,Loader=yaml.SafeLoader)

    print(config)