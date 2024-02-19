import pickle
from .handler import Config


def loadsConfig(bytes: bytes) -> Config:
    """
    Deserialize a Config object from a bytes object using the pickle module.

    Args:
        bytes (bytes): A bytes object containing a serialized Config object.

    Returns:
        Config: The deserialized Config object.
    """

    obj = pickle.loads(bytes)
    r = Config(DICT=obj[0])
    r._meta = obj[1]
    return r


def dumpsConfig(config: Config) -> bytes:
    """
    Serialize a Config object into a bytes object using the pickle module.

    Args:
        config (Config): The Config object to be serialized.

    Returns:
        bytes: The serialized Config object.
    """

    return pickle.dumps((config.DICT, config._meta))
