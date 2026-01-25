from dataclasses import dataclass
from pathlib import Path
from datetime import date
import logging
from typing import Optional
from time import strftime


@dataclass(frozen=True)
class DockerResourceHandler:

    def _setup(self, asset_type: str):
        today_dir = Path.cwd() / "logs" / date.today().isoformat() / asset_type
        today_dir.mkdir(exist_ok=True, parents=True)
        return today_dir

    def persist_image_logs(
        self,
        asset_type: str,
        image_name: Optional[str] = None,
        container_name: Optional[str] = None,
        stream: Optional[str] = "",
        errors: Optional[str] = "",
    ):
        asset_picker = {"image": image_name, "container": container_name}
        file_name = asset_picker[asset_type]
        today_dir = self._setup(asset_type)
        if (today_dir / f"{file_name}.txt").is_file() or (
            today_dir / f"{file_name}_errors.txt"
        ).is_file():
            logging.info("File exists, appending new logs to the file")
            if stream:
                with open(today_dir / f"{file_name}.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ") + stream + "\n")
                    logs_file.close()
            elif errors:
                with open(today_dir / f"{file_name}_errors.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ") + errors + "\n")
                    logs_file.close()
        else:
            logging.info("Writing logs stream to the file")
            if stream:
                with open(today_dir / f"{file_name}.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ") + stream + "\n")
                    logs_file.close()
            elif errors:
                with open(today_dir / f"{file_name}_errors.txt", "a") as logs_file:
                    logs_file.write(strftime("%Y-%m-%d %H:%M:%S ") + errors + "\n")
                    logs_file.close()
