from dataclasses import dataclass
import logging


@dataclass(frozen=True)
class ContainerHandler:

    def build_container(self, image_name: str, name: str):
        container_build = self._client.containers.run(
            image=image_name, name=name, detach=True, stdout=True, stderr=True
        )
        for x in container_build.logs(stream=True, follow=True):
            self.persist_image_logs(
                asset_type="container", container_name=name, stream=x.decode()
            )
        return container_build

    def start_container(self, image_name: str, name: str):
        try:
            container_ref = self._client.containers.get(name)
            if container_ref.status != "running":
                container_ref.start()

            if container_ref.status == "running":
                container_ref.restart()

            for x in container_ref.logs(stream=True, follow=True):
                self.persist_image_logs(
                    asset_type="container", container_name=name, stream=x.decode()
                )
        except Exception as e:
            logging.warning(f"Got {e} exception, starting new container instance ")
            self.build_container(image_name=image_name, name=name)
