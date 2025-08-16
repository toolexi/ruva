import os
from typing import Dict
from pydantic import BaseModel
from ruva.pydanticModels._workspace import ProjectConfigsStruct, ProjManager
import tomlkit


class WorkspaceManager:
    def __init__(self):
        pass

    def initiate_project(self, configs: Dict):
        mainconfig_path = os.getcwd()
        # configs_json = json.loads(configs)
        _dirname = configs["name"]
        configpath = mainconfig_path + "/" + _dirname
        assetConfig = configs["configType"].lower()

        if not os.path.exists(configpath):
            os.mkdir(configpath)
        with open(configpath + "/" + assetConfig + "config.toml", "w") as config_file:
            config_file.write(tomlkit.dumps(configs, sort_keys=False))
        if not os.path.exists(mainconfig_path + "/ruvaconfig.toml"):
            with open(mainconfig_path + "/ruvaconfig.toml", "w") as main_config:
                main_config.write(
                    tomlkit.dumps(
                        ProjManager(project=ProjectConfigsStruct()).model_dump()
                    )
                )
        if not os.path.exists(mainconfig_path + "/.env"):
            with open(mainconfig_path + "/.env", "w") as main_config:
                main_config.write(
                    "#Add your configs here"
                )

    def trigger_configs(self, baseClass: BaseModel):
        configs = baseClass.model_dump()
        self.initiate_project(configs)
