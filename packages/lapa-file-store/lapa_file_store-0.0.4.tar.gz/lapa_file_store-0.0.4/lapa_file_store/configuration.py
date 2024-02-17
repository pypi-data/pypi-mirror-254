import configparser
import os
import sys

from square_logger.main import SquareLogger

try:
    config = configparser.ConfigParser()
    config_file_path = (
        os.path.dirname(os.path.abspath(__file__))
        + os.sep
        + "data"
        + os.sep
        + "config.ini"
    )
    config.read(config_file_path)

    # get all vars and typecast
    config_str_module_name = config.get("GENERAL", "MODULE_NAME")

    config_str_host_ip = config.get("ENVIRONMENT", "HOST_IP")
    config_int_host_port = int(config.get("ENVIRONMENT", "HOST_PORT"))

    config_str_log_file_name = config.get("ENVIRONMENT", "LOG_FILE_NAME")
    config_str_local_storage_folder_path = config.get(
        "ENVIRONMENT", "LOCAL_STORAGE_PATH"
    )
    # initialize logger
    global_object_square_logger = SquareLogger(config_str_log_file_name)
except Exception as e:
    print(
        "\033[91mMissing or incorrect config.ini file.\n"
        "Error details: " + str(e) + "\033[0m"
    )
    sys.exit()

# extra logic for this module

try:
    global_absolute_path_local_storage = os.path.abspath(
        config_str_local_storage_folder_path
    )
    if not os.path.exists(global_absolute_path_local_storage):
        os.makedirs(global_absolute_path_local_storage)
except Exception as e:
    print(
        "\033[91mIncorrect value for LOCAL_STORAGE_PATH in config.ini file.\n"
        "Error details: " + str(e) + "\033[0m"
    )
    sys.exit()
