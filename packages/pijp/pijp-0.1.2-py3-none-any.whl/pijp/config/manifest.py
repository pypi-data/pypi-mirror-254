import logging

from pydantic import BaseModel
import yaml

from pijp.config.pipeline import Pipeline


class Manifest(BaseModel):
    version: int
    pipelines: dict[str, Pipeline] = {}

    @classmethod
    def load_file(cls, file_path: str) -> "Manifest":
        """
        Load and parse the manifest file.

        Args:
            file_path (str): The path to the manifest file.

        Returns:
            Manifest: An instance of the Manifest class populated with the data from the file.
        """

        logging.debug("Loading manifest file from %s", file_path)

        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            return cls(**data)
