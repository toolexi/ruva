from dataclasses import dataclass, field

@dataclass(frozen=True)
class ContainerHandler:

    def get_container_status(self):
        print("Hello")