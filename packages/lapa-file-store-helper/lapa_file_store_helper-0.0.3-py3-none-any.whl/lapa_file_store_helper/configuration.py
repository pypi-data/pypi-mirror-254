import os

from lapa_commons.main import read_configuration_from_file_path

config_file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "data" + os.sep + "config.ini"
ldict_configuration = read_configuration_from_file_path(config_file_path)

# get all vars and typecast
config_str_lapa_file_store_protocol = str(ldict_configuration["ENVIRONMENT"]["LAPA_FILE_STORE_PROTOCOL"])
config_str_lapa_file_store_ip = str(ldict_configuration["ENVIRONMENT"]["LAPA_FILE_STORE_IP"])
config_int_lapa_file_store_port = int(ldict_configuration["ENVIRONMENT"]["LAPA_FILE_STORE_PORT"])
