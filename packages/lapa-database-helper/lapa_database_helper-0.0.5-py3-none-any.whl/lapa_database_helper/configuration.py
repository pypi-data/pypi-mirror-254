import os

from lapa_commons.main import read_configuration_from_file_path

config_file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "data" + os.sep + "config.ini"
ldict_configuration = read_configuration_from_file_path(config_file_path)

# get all vars and typecast
config_str_lapa_database_protocol = str(ldict_configuration["ENVIRONMENT"]["LAPA_DATABASE_PROTOCOL"])
config_str_lapa_database_ip = str(ldict_configuration["ENVIRONMENT"]["LAPA_DATABASE_IP"])
config_int_lapa_database_port = int(ldict_configuration["ENVIRONMENT"]["LAPA_DATABASE_PORT"])
