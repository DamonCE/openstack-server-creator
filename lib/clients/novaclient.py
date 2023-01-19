from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as novaclient

from lib.utils.config import nova_config

def get_nova_from_nova_config():
    
    auth = v3.Password(auth_url=nova_config['auth_url'],
                        username=nova_config['username'],
                        password=nova_config['password'],
                        user_domain_id=nova_config['user_domain_id'],
                        project_domain_id=nova_config['project_id'],
                        project_id=nova_config['project_id']
                        )
    sess = session.Session(auth=auth)
    nova = novaclient.Client(nova_config['version'], session=sess)
    return nova

nova = get_nova_from_nova_config()