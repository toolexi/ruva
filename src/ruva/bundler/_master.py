from dataclasses import dataclass, field, replace
from functools import cached_property
from typing import Literal
import docker

LoadType = Literal["images", "containers"]


@dataclass(frozen=True)
class DockerMaster:
    _client: docker.DockerClient = field(default=None, repr=False)
    _intent: LoadType | None = field(default=None, repr=False)
    # _images: tuple[Any, ...] = field(default_factory=tuple, repr=False)
    # _containers: tuple[Any, ...] = field(default_factory=tuple, repr=False)
    # _loaded_type: str = field(default_factory=str, repr=False)

    def connect(self) -> "DockerMaster":
        return replace(self, _client=docker.from_env())

    def images(self) -> "DockerMaster":
        return replace(self, _intent="images")

    def containers(self) -> "DockerMaster":
        return replace(self, _intent="containers")
    
    @property
    def _get_images_(self):
        images = self._client.images.list()
        return images
    
    @property
    def _get_containers_(self):
        containers = self._client.containers.list()
        return containers
    
    def get(self):
        response_dict = {"images": self._client.images.list(), "containers": self._client.containers.list()}
        return { self._intent : response_dict[self._intent]}
