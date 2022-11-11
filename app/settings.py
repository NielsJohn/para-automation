from dataclasses import dataclass
from pathlib import Path

import toml
from dotenv import load_dotenv


class Environment:
    def __init__(self) -> None:
        if is_docker():
            load_dotenv()
        else:
            env_file = Path().cwd().parent / "environment" / ".env"
            load_dotenv(env_file)
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


def is_docker() -> bool:
    """
    Check if some python code runs from inside a docker container.
    Returns:
        True if yes, False if not.
    """
    cgroup = Path("/proc/self/cgroup")
    return Path('/.dockerenv').is_file() or (cgroup.is_file() and cgroup.read_text().find("docker") > -1)


settings = Settings()
