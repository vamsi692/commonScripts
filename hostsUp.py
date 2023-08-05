#!/usr/bin/env python3

import sys

ips = []

# Function to find IP addresses with the specified word in a file
def openIps(file_path, word):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            List = []
            if word in line:
                count += 1
                List = line.split(" ")
                ips.append(List[1].strip())  # Append the IP address to the 'ips' list, removing any leading/trailing whitespace
    print(count)  # Print the number of lines with the specified word in the file
    return ips  # Return the 'ips' list containing IP addresses with the specified word

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2 and len(sys.argv) != 3:
    # If you want the list of open port IPs as a file, provide the path where the file has to be written as the second argument
    print("Use the following format 'python hostsUp.py <file_path> <write_file_path>")
    sys.exit(0)

# When only one command-line argument is provided (file path) - Display the IPs on the console
if len(sys.argv) == 2:
    ips_list = openIps(sys.argv[1], "open")  # Call the openIps function to get the list of IP addresses
    print("The following are the IPs of the machines with the said port open: \n" + str(ips_list))  # Convert list to a string before printing
else:  # When two command-line arguments are provided (file path and write file path) - Write IPs to the specified file
    ips_list = openIps(sys.argv[1], "open")  # Call the openIps function to get the list of IP addresses
    with open(sys.argv[2], 'w') as file:
        for item in ips_list:
            file.write(str(item) + '\n')  # Write each IP address to a new line in the file
    print("done")
    
