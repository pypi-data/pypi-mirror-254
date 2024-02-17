import configparser
import os

config = configparser.ConfigParser()
config_file_path = (
    os.path.dirname(os.path.abspath(__file__)) + os.sep + "data" + os.sep + "config.ini"
)
config.read(config_file_path)

# get all vars and typecast

config_str_lapa_database_protocol = config.get("ENVIRONMENT", "LAPA_DATABASE_PROTOCOL")
config_str_lapa_database_ip = config.get("ENVIRONMENT", "LAPA_DATABASE_IP")
config_int_lapa_database_port = int(config.get("ENVIRONMENT", "LAPA_DATABASE_PORT"))
