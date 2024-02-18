import comfyconf.readers as readers


class DotDict(dict):
    """
    A dictionary subclass that allows access to its elements using dot notation.

    This class inherits from the built-in `dict` class and enhances it with dot notation access.
    Dot notation allows accessing dictionary elements as attributes, providing more concise syntax.

    Attributes:
        dictionary (dict): The dictionary to be wrapped by the DotDict instance.

    Methods:
        __init__(dictionary: dict) -> None:
            Initialize the DotDict with the given dictionary.

        error_if_numerical_key(dictionary: dict) -> None:
            Recursively checks the dictionary for numerical keys and raises a ValueError if found.

    Examples:
        >>> d = DotDict({'foo': 1, 'bar': {'baz': 2}})
        >>> d.foo
        1
        >>> d.bar.baz
        2

    Note:
        Numerical keys are not allowed, as they can't be accessed using dot notation.
        Attempting to access or set numerical keys with dot notation will result in a SyntaxError.
    """

    def __init__(self, dictionary: dict) -> None:
        """
        Initialize the DotDict with the given dictionary.

        Args:
            dictionary (dict): The dictionary to be wrapped by the DotDict instance.
        """
        self.error_if_numerical_key(dictionary)
        super().__init__(dictionary)

    def __getattr__(*args):
        """
        Retrieve the value of the given attribute.

        Args:
            *args: Variable-length argument list.

        Returns:
            The value associated with the given attribute.

        Raises:
            KeyError: If the attribute does not exist.
        """
        value = dict.__getitem__(*args)
        return DotDict(value) if isinstance(value, dict) else value

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def error_if_numerical_key(self, dictionary: dict) -> None:
        """
        Recursively checks the dictionary for numerical keys and raises a ValueError if found.

        Args:
            dictionary (dict): The dictionary to be checked.

        Raises:
            ValueError: If a numerical key is found in the dictionary.
        """
        if isinstance(dictionary, dict):
            for key, value in dictionary.items():
                if str(key).isnumeric():
                    raise ValueError(
                        f"Numerical keys are not allowed, however one was found: '{key}'"
                    )
                else:
                    self.error_if_numerical_key(value)


def make_config(config_path: str, reader: str = "pyyaml") -> DotDict:
    """
    Create a DotDict configuration object from a configuration file.

    This function reads a configuration file using the specified reader and returns
    a DotDict object representing the configuration.

    Args:
        config_path (str): The path to the configuration file.
        reader (str, optional): The name of the reader to use. Defaults to 'pyyaml'.

    Returns:
        DotDict: A DotDict object representing the configuration read from the file.

    Raises:
        ValueError: If the specified reader is not available.

    Examples:
        >>> config = make_config('config.yaml')
        >>> config.foo.bar
        'value_of_bar'
    """
    reader = readers.get_reader(reader)
    yaml_dict = reader(config_path).read()
    return DotDict(yaml_dict)
