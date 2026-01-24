from .cli.entrypoint import main
from .bundler._master import DockerMaster

if __name__ == "__main__":
    DockerMaster().client.images.pull("hello-world")
    main()
