import sys
import subprocess

# Check if pip is installed
try:
    subprocess.run(["pip", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
except FileNotFoundError:
    print("Error: pip is not installed. Please install pip before running this script.")
    sys.exit(1)

# Install required packages
packages_to_install = ["segno"]

for package in packages_to_install:
    try:
        subprocess.run(["python -m pip", "install", package], check=True)
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Error installing {package}")

print("Installation completed.")
