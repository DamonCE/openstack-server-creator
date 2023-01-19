import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

nova_config = config['NOVA']

default_server_config = config['DEFAULT_SERVER_CONFIG']