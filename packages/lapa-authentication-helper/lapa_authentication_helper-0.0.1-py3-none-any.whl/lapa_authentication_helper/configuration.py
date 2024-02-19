import configparser
import os

config = configparser.ConfigParser()
config_file_path = (
        os.path.dirname(os.path.abspath(__file__)) + os.sep + "data" + os.sep + "config.ini"
)
config.read(config_file_path)

# get all vars and typecast

config_str_lapa_authentication_protocol = config.get("ENVIRONMENT", "LAPA_AUTHENTICATION_PROTOCOL")
config_str_lapa_authentication_ip = config.get("ENVIRONMENT", "LAPA_AUTHENTICATION_IP")
config_str_lapa_authentication_port = int(config.get("ENVIRONMENT", "LAPA_AUTHENTICATION_PORT"))
