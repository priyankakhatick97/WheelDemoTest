#Push action running this script 
import os
import re

def increment_version(version):
    # Split the version into parts
    part =  list((version.split('.')))
    parts = [int(i) for i in part]
    # Increment the last part (patch version)
    parts[-1] += 1
    # Join the parts back into a string
    return '.'.join(map(str, parts))

# Fetch versions from environment variables or file
latest_version = os.getenv('LATEST_VERSION', '1.0.0')
current_version = os.getenv('CURRENT_VERSION', '1.0.0')

if latest_version != current_version:
    print("New version available!")
    print('Hello World!!!')
else:
    print("No new update.")

# Increment the latest version for the next push
new_version = increment_version(latest_version)
print(f"New version set to: {new_version}")
