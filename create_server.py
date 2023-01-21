from lib.clients.openstackclient import openstack
from lib.utils.common_functions import wait
from lib.utils.config import default_server_config

# Choose hostname
name = input("Choose the hostname\n")
name = f"{name}.{default_server_config['host_domain']}"

# Choose image
# Get images openstack
images = openstack.list_images()
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
image = images[choice].id

# Select flavor (atm Standard 1GB)
flavors = openstack.list_flavors()
number = 0
print("Choose a flavor")
for flavor in flavors:
    print(f"{number} - {flavor.name}")
    number += 1

# Get user input for the choice
while True:
    try:
        choice = int(input("Enter the number of the Flavor you would like to choose: "))
        assert 0 <= choice < number
        break
    except (ValueError, AssertionError):
        print("This is not a valid option")

# Select chosen image
flavor = flavors[choice].id


# Create empty list of nics
nics = []

networks = openstack.list_networks()
number = 0
print("Choose the primary network")
for network in networks:
    print(f"{number} - {network.name}")
    number += 1

# Get user input for the choice
while True:
    try:
        choice = int(input("Enter the number of the network you would like to choose: "))
        assert 0 <= choice < number
        break
    except (ValueError, AssertionError):
        print("This is not a valid option")

# Select chosen image
network = networks[choice].id

# Put id into nic dict
nic = {
    "net-id": network
}

# Append nic config to list of nics
nics.append(nic)

# Select keypair
keypair = "openstack"

# Create server
print(f"Start building instance")
new_server = openstack.create_server(name=name, image=image, flavor=flavor, nics=nics, key_name=keypair)

# Get data of the new server
instance = openstack.get_server_by_id(new_server.id)

# While instance is building
while instance.status == "BUILD":
    instance = openstack.get_server_by_id(instance.id)
    print("Instance is building...")
    wait()
print("Instance is done building")