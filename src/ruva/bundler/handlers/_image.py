from dataclasses import dataclass
from typing import Dict, Optional
import os

images_parent_dir = os.path.dirname(os.path.dirname(__file__)) + "/images"


@dataclass(frozen=True)
class ImageHandler:

    def pull_image(self, repo_path: str):
        return self._client.images.pull(repo_path)

    def remove_image(self, image_name: str, force: bool = False):
        return self._client.images.remove(image_name, force=force)

    def build_image(
        self,
        variant: str,
        build_args: Optional[Dict[str, str]] = None,
        tag: str = "latest",
        file_path: str = images_parent_dir,
    ):
        image_variants = {
            "notebook": "/notebook",
            "workflow": "/Dockerfile.notebook.dev",
        }
        docker_image_path = file_path + image_variants[variant]
        image_name, logs = self._client.images.build(
            path=docker_image_path, tag=tag, quiet=False
        )
        for lg in logs:
            if "stream" in lg:
                self.persist_image_logs(
                    asset_type="image", image_name=tag, stream=lg["stream"].rstrip()
                )
            elif "error" in lg:
                self.persist_image_logs(
                    asset_type="image", image_name=tag, errors=lg["error"].rstrip()
                )
        return image_name

    def build_custom_image(self, image_path: str):
        print(images_parent_dir)
