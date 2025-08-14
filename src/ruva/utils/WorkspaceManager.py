import os
from typing import Dict
from pydantic import BaseModel
import json
from ruva.pydanticModels._workspace import ProjectConfigsStruct

# CONFIG_FILE = os.getcwd + "/" + Path("ruvaconfig.yaml")


class WorkspaceManager:
    def __init__(self):
        pass

    def InitiateProject(self, configs: Dict, _dirname: str):
        mainconfig_path = os.getcwd()
        configpath = mainconfig_path + "/" + _dirname
        assetConfig = configs["configType"].lower()

        if not os.path.exists(configpath):
            os.mkdir(configpath)
        with open(configpath + "/" + assetConfig + "config.json", "w") as config_file:
            config_file.write(json.dumps(configs, indent=4, sort_keys=False))
        if not os.path.exists(mainconfig_path + "/ruvaconfig.json"):
            with open(mainconfig_path + "/ruvaconfig.json", "a") as main_config:
                main_config.write(
                    json.dumps(
                        ProjectConfigsStruct().model_dump(), indent=4, sort_keys=False
                    )
                )

    def triggerConfigs(self, baseClass: BaseModel):
        configs = baseClass.model_dump()
        _dirname = configs["name"]
        self.InitiateProject(configs, _dirname)
