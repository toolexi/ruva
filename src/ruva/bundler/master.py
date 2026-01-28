from dataclasses import dataclass, field, replace
from typing import Literal
import docker
from .handlers import ImageHandler, ContainerHandler, DockerResourceHandler
import secrets

LoadType = Literal["images", "containers"]

token = secrets.token_hex(24)


@dataclass(frozen=True)
class DockerMaster(ImageHandler, ContainerHandler, DockerResourceHandler):
    _client: docker.DockerClient = field(default=None, repr=False)
    _intent: LoadType | None = field(default=None, repr=False)

    def connect(self) -> "DockerMaster":
        return replace(self, _client=docker.from_env())

    def images(self) -> "DockerMaster":
        return replace(self, _intent="images")

    def containers(self) -> "DockerMaster":
        return replace(self, _intent="containers")

    @property
    def _get_images(self):
        images = self._client.images.list()
        return images

    @property
    def _get_containers(self):
        containers = self._client.containers.list()
        return containers

    def get(self):
        response_dict = {
            "images": self._client.images.list(),
            "containers": self._client.containers.list(),
        }
        return {self._intent: response_dict[self._intent]}


# print(DockerMaster().connect().images().get())
# DockerMaster(image_name="hello-world").connect().remove_image()

# DockerMaster().connect().get_container_status()

# print(DockerMaster().connect().build_image(variant="notebook", tag="jupyter_nb_image"))

print("http://127.0.0.1:8888/lab?token=" + token)

print(
    DockerMaster()
    .connect()
    .start_container(
        image_name="jupyter_nb_image",
        name="sample_container",
        command=[
            "jupyter",
            "lab",
            "--ip=0.0.0.0",
            "--port=8888",
            "--no-browser",
            "--allow-root",
            f"--IdentityProvider.token={token}",
        ],
    )
)

# print(DockerMaster().build_image())
