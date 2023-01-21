import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

openstack_config = config['OPENSTACK']

default_server_config = config['DEFAULT_SERVER_CONFIG']