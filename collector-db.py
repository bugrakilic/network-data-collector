import sqlite3
from netmiko import ConnectHandler

# Define the device to connect to
device = {
    "host": "192.168.1.1",
    "username": "myuser",
    "password": "mypass",
    "device_type": "cisco_ios",
}

# Connect to the device
net_connect = ConnectHandler(**device)

# Execute a command on the device
output = net_connect.send_command("show version")

# Disconnect from the device
net_connect.disconnect()

# Connect to the database
conn = sqlite3.connect("mydatabase.db")

# Create a cursor
cursor = conn.cursor()

# Execute a query to create the table if it does not exist
cursor.execute(
    "CREATE TABLE IF NOT EXISTS device_output (host text, output text)"
)

# Insert the output into the table
cursor.execute("INSERT INTO device_output VALUES (?,?)", (device["host"], output))

# Save the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
