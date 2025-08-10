import os
from typing import Dict
import yaml
from pydantic import BaseModel


class WorkspaceManager:
    def __init__(self):
        pass

    def InitiateProject(self, configs: Dict, _dirname: str):
        configpath = os.getcwd() + "/" + _dirname
        if not os.path.exists(configpath):
            os.mkdir(configpath)
        with open(configpath + "/ruvaconfig.yml", "w") as config_file:
            config_file.write(yaml.dump(configs, indent=4, sort_keys=False))

    def triggerConfigs(self, baseClass: BaseModel):
        commandStruct = baseClass()
        configs = commandStruct.model_dump()
        _dirname = configs["configType"]
        self.InitiateProject(commandStruct.model_dump(), _dirname)
