import os
from dataclasses import dataclass

import toml
from dotenv import load_dotenv


class Environment:
    def __init__(self) -> None:
        load_dotenv()
        self._internal_path = os.getenv("INTERNAL_PATH")

    @property
    def internal_path(self) -> str | None:
        return self._internal_path


@dataclass
class Settings:
    """A class to store settings."""

    env: Environment = Environment()

    def __post_init__(self) -> None:
        with open("core/config.toml", "r") as file:
            self.toml_content = toml.load(file)

    @property
    def para_folders(self) -> list[str]:
        return self.toml_content.get("para").get("folders")

    @property
    def task_list(self) -> list[str]:
        return self.toml_content.get("app").get("task_list")

    @property
    def internal_path(self) -> str:
        return self.env.internal_path


settings = Settings()
