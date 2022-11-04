from dataclasses import dataclass

import toml


@dataclass
class Settings:
    """A class to store settings."""

    def __post_init__(self) -> None:
        with open('core/config.toml', 'r') as file:
            self.toml_content = toml.load(file)

    @property
    def para_folders(self) -> list[str]:
        return self.toml_content.get("para").get("folders")

    @property
    def task_list(self) -> list[str]:
        return self.toml_content.get("app").get("task_list")


settings = Settings()
