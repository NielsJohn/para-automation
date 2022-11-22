from dataclasses import dataclass
from pathlib import Path

import toml
from pydantic import BaseSettings


def is_docker() -> bool:
    """
    Check if some python code runs from inside a docker container.
    Returns:
        True if yes, False if not.
    """
    cgroup = Path("/proc/self/cgroup")
    return Path('/.dockerenv').is_file() or (cgroup.is_file() and cgroup.read_text().find("docker") > -1)


@dataclass
class ParaSettings:
    """A class to store settings."""

    def __post_init__(self) -> None:
        with open("core/config.toml", "r") as file:
            self.toml_content = toml.load(file)

    @property
    def para_folders(self) -> list[str]:
        return self.toml_content.get("para").get("folders")

    @property
    def task_list(self) -> list[str]:
        return self.toml_content.get("app").get("task_list")


para_settings = ParaSettings()


class Settings(BaseSettings):
    PARA_FOLDERS: list[str] = para_settings.para_folders
    TASK_LIST: list[str] = para_settings.task_list
    INTERNAL_PATH: str

    class Config:
        if not is_docker():
            env_file = Path().cwd() / "environment" / ".env"
        else:
            ...


settings = Settings()
