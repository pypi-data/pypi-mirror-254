from abc import ABC, abstractmethod
from pathlib import Path
import yaml


class Reader(ABC):
    """
    Abstract base class for configuration file readers.

    This class defines the interface for configuration file readers. Subclasses must implement
    the read method to provide functionality for reading configuration files.

    Attributes:
        config_path (Path): The path to the configuration file.

    Methods:
        __init__(config_path: str) -> None:
            Initialize the Reader with the given configuration file path.

        _check_path() -> None:
            Check if the configuration file exists. Raises FileNotFoundError if not found.

        read() -> dict:
            Abstract method to be implemented by subclasses for reading configuration files.

    """

    def __init__(self, config_path: str) -> None:
        """
        Initialize the Reader with the given configuration file path.

        Args:
            config_path (str): The path to the configuration file.
        """
        self.config_path = Path(config_path)

    def _check_path(self) -> None:
        """
        Check if the configuration file exists.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
        """
        if not self.config_path.exists():
            raise FileNotFoundError(f"{self.config_path} was not found")

    @abstractmethod
    def read(self) -> dict:
        """
        Abstract method to be implemented by subclasses for reading configuration files.

        Returns:
            dict: A dictionary containing the configuration data.
        """
        pass


class PyYaml(Reader):
    """
    Configuration file reader for YAML format using PyYAML library.

    This class inherits from Reader and implements the read method to read configuration
    files in YAML format using the PyYAML library.

    """

    def __init__(self, config_path: str) -> None:
        """
        Initialize the PyYaml reader with the given configuration file path.

        Args:
            config_path (str): The path to the configuration file.
        """
        super().__init__(config_path)

    def read(self) -> dict:
        """
        Read the configuration file in YAML format using PyYAML library.

        Returns:
            dict: A dictionary containing the configuration data.
        """
        self._check_path()
        with open(self.config_path) as f:
            return yaml.safe_load(f)


# Dictionary to map reader names to reader classes
available_readers = {
    "pyyaml": PyYaml,
}

# Try importing Ruamel YAML library
try:
    from ruamel.yaml import YAML

    class Ruamel(Reader):
        """
        Configuration file reader for YAML format using Ruamel YAML library.

        This class inherits from Reader and implements the read method to read configuration
        files in YAML format using the Ruamel YAML library.

        """

        def __init__(self, config_path: str) -> None:
            """
            Initialize the Ruamel reader with the given configuration file path.

            Args:
                config_path (str): The path to the configuration file.
            """
            super().__init__(config_path)

        def read(self) -> dict:
            """
            Read the configuration file in YAML format using Ruamel YAML library.

            Returns:
                dict: A dictionary containing the configuration data.
            """
            self._check_path()
            yaml = YAML(typ="safe")
            return yaml.load(self.config_path)

    available_readers["ruamel"] = Ruamel

except ImportError:
    pass


def get_reader(reader: str):
    """
    Get the configuration file reader class based on the provided reader name.

    Args:
        reader (str): The name of the reader.

    Returns:
        Reader: An instance of the configuration file reader class corresponding to the provided name.

    Raises:
        ValueError: If the provided reader name is not valid.
    """
    try:
        return available_readers[reader]
    except KeyError:
        raise ValueError(
            f"{reader} is not a reader, available readers are {available_readers.keys()}"
        )
