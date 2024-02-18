from . import ContainerImageList, ContainerImage
import logging
import os
import tempfile
import requests
import tarfile
import typer

from docker import DockerClient

logger = logging.getLogger("otimages." + os.path.basename(__file__))


class xECMMonImages(ContainerImageList):
    def __init__(
        self,
        version: str,
        docker_client: DockerClient,
        repository: str = "artifactory.otxlab.net",
        path: str = "/ot2-paas-dev/ecmcontainerization/",
        latest: bool = False,
    ):
        self.version = version
        self.repository = repository
        self.latest = latest
        self.docker_client = docker_client

        stage = "latest" if self.latest else "released"

        self.path = path + stage

        self.images = self.__get_images()

    def __get_images(self):
        all_images = []
        all_images.append(
            ContainerImage(
                repository=self.repository,
                path=self.path,
                name="xecm-mon",
                version="latest" if self.latest else self.version,
                version_overwrite="stable",
                docker_client=self.docker_client,
            )
        )
        return all_images
