import re

def increment_version(version):
    # Split the version into parts
    parts = list(map(int, version.split('.')))
    # Increment the last part (patch version)
    parts[-1] += 1
    # Join the parts back into a string
    return '.'.join(map(str, parts))

# Read the current version from version.txt
with open('version.txt', 'r') as f:
    latest_version = f.read().strip()

# Hard-code the current version
current_version = '1.0.0'

print(f"Latest Version: {latest_version}")
print(f"Current Version: {current_version}")

if latest_version != current_version:
    print("New version available!")
else:
    print("No new update.")

# Increment the latest version for the next push
new_version = increment_version(latest_version)
print(f"New version set to: {new_version}")

# Write the new version back to version.txt
with open('version.txt', 'w') as f:
    f.write(new_version)
