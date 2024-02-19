from typing import Union, Dict, Optional, Callable
from functools import wraps
import yaml
import os
import json
import tempfile
from typing import Any, Dict, Tuple, Literal
from llm_party.service.session_service import (
    start_session,
    start_session_with_user_first_message,
    initialize_chat_session
)

from ..model.session_models import ChatSession


def is_yaml(file_path):
    return file_path.endswith(".yaml") or file_path.endswith(".yml")


def convert_yaml_to_temp_json(yaml_file_path: str) -> str:
    """Converts a YAML file to a temporary JSON file. The temporary file will be deleted after the program exits.

    Args:
        yaml_file_path (str): Yaml file path

    Returns:
        str: Json file path of the converted yaml file.
    """
    with open(yaml_file_path, "r") as file:
        config_dict = yaml.safe_load(file)

    temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json")
    json.dump(config_dict, temp_file)
    temp_file.flush()

    return temp_file.name


def yaml_acceptable(func):
    """
    A decorator that preprocesses the 'config_file_path' argument for the decorated function.

    If the 'config_file_path' argument points to a YAML file, this decorator converts the file to a temporary JSON format before calling the original function. The conversion is performed using the 'convert_yaml_to_temp_json' function, and the check for YAML file format is done using the 'is_yaml' function.

    Parameters:
    func (Callable): The function to be decorated. It is expected that this function will have 'config_file_path' as one of its arguments.

    Returns:
    Callable: A wrapper function that incorporates the preprocessing step and then calls the original function with the updated arguments.

    Usage:
    @preprocess_config
    def my_function(config_file_path, *args, **kwargs):
        # Function implementation
        pass
    """

    def wrapper(*args, **kwargs):
        # Extract and preprocess config_file_path
        config_file_path = args[0] if args else kwargs.get("config_file_path")
        is_yaml_config = is_yaml(config_file_path)
        if config_file_path and is_yaml_config:
            json_config_file_path = convert_yaml_to_temp_json(config_file_path)
        else:
            json_config_file_path = config_file_path

        if args:
            args = (json_config_file_path,) + args[1:]
        else:
            kwargs["config_file_path"] = json_config_file_path

        try:
            # Call the original function
            ret = func(*args, **kwargs)
        finally:
            if is_yaml_config:
                os.remove(json_config_file_path)
        return ret

    return wrapper

def config_dict_or_path(func):
    """
    A decorator that preprocesses the 'config' argument for the decorated function.

    If the 'config' argument is a dictionary, this decorator converts the dictionary to a temporary JSON file before calling the original function. If the 'config' argument is a string, it is assumed to be a file path and is passed directly to the original function.

    Parameters:
    func (Callable): The function to be decorated. It is expected that this function will have 'config' as one of its arguments.

    Returns:
    Callable: A wrapper function that incorporates the preprocessing step and then calls the original function with the updated arguments.
    """
    @wraps(func)
    def wrapper(config: Union[str, Dict], *args, **kwargs):
        if isinstance(config, dict):
            temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json")
            json.dump(config, temp_file)
            temp_file.flush()
            config_file_path = temp_file.name
        else:
            config_file_path = config

        try:
            # Call the original function
            ret = func(config_file_path, *args, **kwargs)
        finally:
            if isinstance(config, dict):
                os.remove(config_file_path)
        return ret

    return wrapper

def config_chat_session_or_dict_or_path_or_yaml(func):
    """
    Decorator function that handles the configuration of a chat session.
    It accepts a configuration parameter that can be a string, a dictionary, or a ChatSession object.
    If the configuration is a ChatSession object, it is converted to a temporary JSON file.
    If the configuration is a dictionary, it is also converted to a temporary JSON file.
    If the configuration is a YAML file, it is converted to a temporary JSON file.
    Otherwise, the configuration is treated as a file path.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.

    Raises:
        FileNotFoundError: If the configuration file path is not found.
    """
    @wraps(func)
    def wrapper(config: Union[str, Dict, ChatSession], *args, **kwargs):
        if isinstance(config, ChatSession):
            temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json")
            json.dump(config.to_dict(), temp_file)
            temp_file.flush()
            config_file_path = temp_file.name
        elif isinstance(config, dict):
            temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json")
            json.dump(config, temp_file)
            temp_file.flush()
            config_file_path = temp_file.name
        else:
            if is_yaml(config):
                config_file_path = convert_yaml_to_temp_json(config)
            else:
                config_file_path = config

        try:
            # Call the original function
            ret = func(config_file_path, *args, **kwargs)
        finally:
            if isinstance(config, (dict, ChatSession)) or is_yaml(config):
                os.remove(config_file_path)
        return ret

    return wrapper

@config_chat_session_or_dict_or_path_or_yaml
def init_chat_session(config: Union[str, Dict, ChatSession]):
    return initialize_chat_session(config)

@config_chat_session_or_dict_or_path_or_yaml
def start_session_controller(config: Union[str, Dict, ChatSession], save_dir:str=None, save_file_name:str=None, pretty_print:bool=False, save_yaml:bool=False, output: Optional[Callable[[str], None]] = None):
    chat_session, saved_file_path = start_session(config, save_dir, save_file_name, pretty_print, save_yaml, output)

    return chat_session, saved_file_path

@config_chat_session_or_dict_or_path_or_yaml
def start_session_with_first_message_controller(
    config: Union[str, Dict, ChatSession],
    first_message: str,
    sender_name: str,
    sender_role: str,
    sender_type: Literal["Human", "Agent"],
    sender_attendee_params: dict,
    save_dir:str=None,
    save_file_name: str=None,
    pretty_print:bool=False,
    save_yaml:bool=False,
    output: Optional[Callable[[str], None]] = None
) -> Tuple[ChatSession, str]:
    chat_session, saved_file_path = start_session_with_user_first_message(
        config,
        first_message,
        sender_name,
        sender_role,
        sender_type,
        sender_attendee_params,
        save_dir,
        save_file_name,
        pretty_print,
        save_yaml,
        output
    )

    return chat_session, saved_file_path
