import configparser
import os

config = configparser.ConfigParser()
config_file_path = (
    os.path.dirname(os.path.abspath(__file__)) + os.sep + "data" + os.sep + "config.ini"
)
config.read(config_file_path)

# get all vars and typecast

config_str_lapa_file_store_protocol = config.get(
    "ENVIRONMENT", "LAPA_FILE_STORE_PROTOCOL"
)
config_str_lapa_file_store_ip = config.get("ENVIRONMENT", "LAPA_FILE_STORE_IP")
config_int_lapa_file_store_port = int(config.get("ENVIRONMENT", "LAPA_FILE_STORE_PORT"))
