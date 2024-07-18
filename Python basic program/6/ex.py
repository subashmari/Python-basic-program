import re

string = "Ansar@manju@2023_Sibi.Subash#ali.mani"

# Extract username
username = re.findall(r'^\w+', string)[0]
print(f"Username: {username}")

# Extract email domain
domain = re.findall(r'@\w+', string)[0]
print(f"Email domain: {domain}")

# Extract year
year = re.findall(r'\d{4}', string)[0]
print(f"Year: {year}")

# Extract first name
first_name = re.findall(r'(?<=_)\w+', string)[0]
print(f"First name: {first_name}")

# Extract last name
last_name = re.findall(r'(?<=#)\w+', string)[0]
print(f"Last name: {last_name}")
