from dataclasses import dataclass, field
from ...bundler._master import DockerMaster

@dataclass(frozen=True)
class ImageHandler:
    image_name: str = field(default=str, repr=False)

    def pull_image(self):
        return self.client.images.pull(self.image_name)

    def remove_image(self, force: bool = False):
        return self.client.images.remove(self.image_name, force=force)


handler = ImageHandler(image_name="hello-world")
