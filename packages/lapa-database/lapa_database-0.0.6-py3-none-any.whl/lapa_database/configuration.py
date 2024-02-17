import configparser
import importlib
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
    config_str_host_ip = config.get("ENVIRONMENT", "HOST_IP")
    config_int_host_port = int(config.get("ENVIRONMENT", "HOST_PORT"))
    config_str_db_ip = config.get("ENVIRONMENT", "DB_IP")
    config_int_db_port = int(config.get("ENVIRONMENT", "DB_PORT"))
    config_str_db_username = config.get("ENVIRONMENT", "DB_USERNAME")
    config_str_db_password = config.get("ENVIRONMENT", "DB_PASSWORD")
    config_str_log_file_name = config.get("ENVIRONMENT", "LOG_FILE_NAME")
    config_bool_create_schema = eval(config.get("ENVIRONMENT", "CREATE_SCHEMA"))
    config_str_database_module_name = config.get("ENVIRONMENT", "DATABASE_PACKAGE_NAME")
except Exception as e:
    print(
        "\033[91mMissing or incorrect config.ini file, have you tried creating it from config.example.ini?\n"
        "Error details: " + str(e) + "\033[0m"
    )
    sys.exit()

global_object_square_logger = SquareLogger("lapa_database")

# extra logic for this module

try:
    database_structure_module = importlib.import_module(config_str_database_module_name)
    database_structure_main_file = importlib.import_module(
        config_str_database_module_name + ".main"
    )
except Exception as e:
    print(
        "\033[91mUnable to import "
        + config_str_database_module_name
        + ".\n"
        + "This package needs a specialized package with the pydantic models of all tables.\n"
        + "Install it and update config.ini -> `DATABASE_PACKAGE_NAME` to initiate this package.\n"
        + "Error details: "
        + str(e)
        + "\033[0m"
    )
    sys.exit()
