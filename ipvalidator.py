import re  # Import regular expression module

# Function to validate IPv4 address
def validate_ipv4(ip):
    # Regular expression pattern to match IPv4 address format
    # IPv4 format: four numbers separated by periods (0-255 each)
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
              r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
              r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
              r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None  # Return True if matched, False if not

# Function to validate IPv6 address
def validate_ipv6(ip):
    # Regular expression pattern to match IPv6 address format
    # IPv6 format: 8 groups of 1 to 4 hex digits separated by colons
    pattern = r'^[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){7}$'
    return re.match(pattern, ip) is not None  # Return True if matched, False if not

# Function to check if the IP address is valid IPv4 or IPv6
def validate_ip_address(ip):
    # Check if it's a valid IPv4 address
    if validate_ipv4(ip):
        print(f"{ip} is a valid IPv4 address.")
    # Check if it's a valid IPv6 address
    elif validate_ipv6(ip):
        print(f"{ip} is a valid IPv6 address.")
    else:
        print(f"{ip} is not a valid IPv4 or IPv6 address.")  # If neither IPv4 nor IPv6

# Ask the user to input an IP address
user_input = input("Enter an IP address to validate: ")

# Call the validation function to check the IP address
validate_ip_address(user_input)
