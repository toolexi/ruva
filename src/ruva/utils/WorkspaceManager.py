import os
from typing import Dict
from pydantic import BaseModel
from ruva.pydanticModels._workspace import (
    ProjectConfigsStruct,
    ProjManager,
    AgentManager,
    AgentStruct,
)
import tomlkit


class WorkspaceManager:
    def __init__(self):
        self.mainconfig_path = os.getcwd()

    def initiate_project(self, configs: Dict):
        _dirname = configs["name"]
        assetConfig = configs["configType"]
        configpath = self.mainconfig_path + f"/{assetConfig}s/" + _dirname
        assetconfigpath = configpath.rsplit("/", 1)[0] + f"/{assetConfig}config.toml"

        if not os.path.exists(configpath):
            os.makedirs(configpath)
        with open(configpath + "/config.toml", "w") as config_file:
            config_file.write(tomlkit.dumps(configs, sort_keys=False))
        if not os.path.exists(self.mainconfig_path + "/ruvaconfig.toml"):
            with open(self.mainconfig_path + "/ruvaconfig.toml", "w") as main_config:
                main_config.write(
                    tomlkit.dumps(
                        ProjManager(project=ProjectConfigsStruct()).model_dump()
                    )
                )
        if not os.path.exists(self.mainconfig_path + "/.env"):
            with open(self.mainconfig_path + "/.env", "w") as main_config:
                main_config.write("#Add your configs here")
        agentdump = AgentManager(agentName=AgentStruct(name=_dirname)).model_dump()
        agentdump[_dirname] = agentdump.pop('agentName')
        if not os.path.exists(assetconfigpath):
            with open(assetconfigpath, "a") as asset_config:
                asset_config.write(
                    tomlkit.dumps(
                        agentdump
                    )
                )

    def trigger_configs(self, base_class: BaseModel):
        configs = base_class.model_dump()
        self.initiate_project(configs)

    def generate_prompt_config(self, target: str, base_class: BaseModel):
        pass
