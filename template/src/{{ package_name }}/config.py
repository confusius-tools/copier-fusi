"""Configuration loader for paths and processing options."""

import tomllib
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PathsConfig:
    """Paths to data and results directories.

    TODO: Add project-specific path fields here and wire them up in load_config().
    """

    data_root: Path
    results_root: Path

    def __post_init__(self):
        """Ensure the results directory exists."""
        self.results_root.mkdir(parents=True, exist_ok=True)


@dataclass
class Config:
    """Top-level configuration object."""

    paths: PathsConfig


def _find_config_path(filename: str = "config.toml") -> Path:
    """Search for the configuration file in the current and parent directories."""
    for path in [Path.cwd(), *Path.cwd().parents]:
        candidate = path / filename
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"No {filename} found in {Path.cwd()} or any parent.")


def load_config(config_path: str | Path | None = None) -> Config:
    """Load configuration from a TOML file.

    Parameters
    ----------
    config_path : str or Path, optional
        Path to the configuration file. If ``None``, defaults to the first
        ``"config.toml"`` found in the current directory or any parent.

    Returns
    -------
    Config
        Configuration object with loaded settings.
    """
    if config_path is None:
        config_path = _find_config_path()

    with open(config_path, "rb") as f:
        config_dict = tomllib.load(f)

    return Config(
        paths=PathsConfig(
            data_root=Path(config_dict["paths"]["data_root"]),
            results_root=Path(config_dict["paths"]["results_root"]),
        ),
    )


# Default config instance for convenient imports.
CONFIG = load_config()
