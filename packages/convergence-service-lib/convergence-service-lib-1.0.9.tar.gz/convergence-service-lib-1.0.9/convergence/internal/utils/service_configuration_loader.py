import os
from typing import Dict

import yaml


def load_service_configuration(default_config_path, profile_config_path):
    default_config = __load_config_file(default_config_path)

    if profile_config_path is not None:
        profile_config = __load_config_file(profile_config_path)
        merged = __merge_config_files(default_config.copy(), profile_config)

        return __swap_environment_variables_in_config(merged)

    return __swap_environment_variables_in_config(default_config)


def __load_config_file(config_path) -> Dict:
    result = None

    with open(config_path, 'r') as yaml_config:
        result = yaml.safe_load(yaml_config)

    if result is None:
        raise ValueError(f'Unable to load config file at path: {config_path}')

    return result


def __merge_config_files(result_config: Dict, profile_config: Dict):
    # TODO: Unit tests
    for key in profile_config:
        if key in result_config:
            value = profile_config[key]
            if isinstance(value, dict):
                result_config[key] = __merge_config_files(result_config[key], value)
            else:
                result_config[key] = profile_config[key]
        else:
            result_config[key] = profile_config[key]

    return result_config


def __swap_environment_variables_in_config(config: Dict):
    swaps = {}
    for key in config:
        value = config[key]
        if isinstance(value, dict):
            __swap_environment_variables_in_config(value)
        elif isinstance(value, str):
            if value.startswith("${") and value.endswith('}'):
                variable_name = value[2:-1]
                if variable_name not in os.environ:
                    raise ValueError(f'The environment variable {variable_name} is not defined.')
                swaps[key] = os.environ[variable_name]

    for key in swaps:
        config[key] = swaps[key]

    return config
