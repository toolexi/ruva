import os
from typing import Dict
import json
import yaml


class WorkspaceManager():
    def __init__(self):
        pass
        # super().__init__(**data)

    def InitiateProject(self, configs: Dict):
        configpath = os.getcwd()
        print(configpath)
        with open(configpath+"/ruvaconfig.yml",'w') as config_file:
            config_file.write(yaml.dump(configs, indent=4, sort_keys=False))
