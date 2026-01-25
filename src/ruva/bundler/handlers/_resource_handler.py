from dataclasses import dataclass
from pathlib import Path
from datetime import date,time
import os
import logging
from typing import Optional
from time import gmtime, strftime

@dataclass(frozen=True)
class DockerResourceHandler:

    def _setup(self):
        main_dir = Path.cwd()
        logs_path = Path.cwd() / "logs"
        today_dir = logs_path / date.today().isoformat()
        today_dir.mkdir(exist_ok=True, parents=True)
        return logs_path, main_dir, today_dir

    def persist_image_logs(self, image_name:str, stream: Optional[str]="", errors: Optional[str]=""):
        logs_path, main_dir, today_dir = self._setup()
        if (today_dir/f"{image_name}.txt").is_file() or (today_dir/f"{image_name}_errors.txt").is_file():
            logging.info("File exists, appending new logs to the file")
            if stream:
                with open(today_dir/f"{image_name}.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ", gmtime()) + stream + "\n")
                    logs_file.close()
            elif errors:
                with open(today_dir/f"{image_name}_errors.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ", gmtime()) + errors + "\n")
                    logs_file.close()
        else:
            logging.info("Writing logs stream to the file")
            if stream:
                with open(today_dir/f"{image_name}.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ", gmtime()) + stream + "\n")
                    logs_file.close()
            elif errors:
                with open(today_dir/f"{image_name}_errors.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ", gmtime()) + errors + "\n")
                    logs_file.close()



