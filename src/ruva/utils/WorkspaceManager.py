import os
from typing import Dict
from pydantic import BaseModel
import json
from ruva.pydanticModels._workspace import ProjectConfigsStruct


class WorkspaceManager:
    def __init__(self):
        pass

    def initiate_project(self, configs: Dict):
        mainconfig_path = os.getcwd()
        configs_json = json.loads(configs)
        _dirname = configs_json["name"]
        configpath = mainconfig_path + "/" + _dirname
        assetConfig = configs_json["configType"].lower()

        if not os.path.exists(configpath):
            os.mkdir(configpath)
        with open(configpath + "/" + assetConfig + "config.json", "w") as config_file:
            config_file.write(configs)
        if not os.path.exists(mainconfig_path + "/ruvaconfig.json"):
            with open(mainconfig_path + "/ruvaconfig.json", "a") as main_config:
                main_config.write(ProjectConfigsStruct().model_dump_json(indent=4))

    def trigger_configs(self, baseClass: BaseModel):
        configs = baseClass.model_dump_json(indent=4)
        self.initiate_project(configs)
