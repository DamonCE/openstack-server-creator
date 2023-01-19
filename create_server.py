from lib.clients.novaclient import nova
from lib.utils.common_functions import wait
from lib.utils.config import default_server_config

# Choose hostname
name = input("Choose the hostname\n")
name = f"{name}.{default_server_config['host_domain']}"

# Choose image
# Get images from glance
images = nova.glance.list()
number = 0
print("Choose an Operating System")

# Print images to screen and output their index number
for image in images:
    print(f"{number} - {image.name}")
    number += 1

# Get user input for the choice
while True:
    try:
        choice = int(input("Enter the number of the OS you would like to choose: "))
        assert 0 <= choice < number
        break
    except (ValueError, AssertionError):
        print("This is not a valid option")

# Select chosen image
image = images[choice]

# Select flavor (atm Standard 1GB)
flavors = nova.flavors.list()
flavor = flavors[0]

# Create empty list of nics
nics = []

# Retrieve network from neutron with name
network = nova.neutron.find_network("net-public")

# Put id into nic dict
nic = {
    "net-id": network.id
}

# Append nic config to list of nics
nics.append(nic)

# Select keypair
keypair = "openstack"

# Create server
print(f"Start building instance with {image.name}")
new_server = nova.servers.create(name=name, image=image, flavor=flavor, nics=nics, key_name=keypair)

# Get data of the new server
instance = nova.servers.get(new_server.id)

# While instance is building
while instance.status == "BUILD":
    instance = nova.servers.get(instance.id)
    print("Instance is building...")
    wait()
print("Instance is done building")