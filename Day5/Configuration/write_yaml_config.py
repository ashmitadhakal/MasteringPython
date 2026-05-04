import yaml

from pathlib import Path

config = {
    'owner':{
        'name':'Bob Smith',
        'email':'bob.smith@coolcompany.com'
    },
    'org':{'name':'Cool Company'}
}

config_file_path = Path("config.yaml")

with config_file_path.open("w",encoding="UTF-8") as config_file:
    config_yaml = yaml.dump(config)
    config_file.write(config_yaml)
