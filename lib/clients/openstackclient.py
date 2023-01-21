from keystoneauth1.identity import v3
from keystoneauth1 import session
from openstack import connection as conn

from lib.utils.config import openstack_config

def get_openstack_from_openstack_config():
    
    auth = v3.Password(auth_url=openstack_config['auth_url'],
                        username=openstack_config['username'],
                        password=openstack_config['password'],
                        user_domain_id=openstack_config['user_domain_id'],
                        project_domain_id=openstack_config['project_id'],
                        project_id=openstack_config['project_id']
                        )
    sess = session.Session(auth=auth)
    openstack = conn.Connection(openstack_config['version'], session=sess)
    
    return openstack

openstack = get_openstack_from_openstack_config()