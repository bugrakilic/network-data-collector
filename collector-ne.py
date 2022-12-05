from netmiko import ConnectHandler

# Define the device to connect to
device = {
    "host": "192.168.1.1",
    "username": "myuser",
    "password": "mypass",
    "device_type": "cisco_ios",
    "use_ssh": True,
}

# Connect to the device
net_connect = ConnectHandler(**device)

# Execute a command on the device
output = net_connect.send_command("show version")

# Print the output
print(output)

# Disconnect from the device
net_connect.disconnect()

'''
# Device parameters are written in a csv file. 

import csv
from netmiko import ConnectHandler

# Open the CSV file with the device parameters
with open("devices.csv", "r") as devices:
    # Read the device parameters from the CSV file
    reader = csv.DictReader(devices)

    # Loop through the device rows
    for row in reader:
        # Define the device parameters
        device = {
            "host": row["host"],
            "username": row["username"],
            "password": row["password"],
            "device_type": row["device_type"],
        }

        # Establish an SSH connection to the device
        net_connect = ConnectHandler(**device)

        # Execute the 'show version' command on the device
        output = net_connect.send_command("show version")

        # Print the command output
        print(output)

        # Close the SSH connection
        net_connect.disconnect()
'''