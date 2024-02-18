[![CI](https://github.com/infrasonar/appliance-manager/workflows/CI/badge.svg)](https://github.com/infrasonar/appliance-manager/actions)
[![Release Version](https://img.shields.io/github/release/infrasonar/appliance-manager)](https://github.com/infrasonar/appliance-manager/releases)


# InfraSonar Appliance Manager

This tool simplifies the installation and management of InfraSonar appliances. It streamlines the process of setting up and running your InfraSonar infrastructure, making it easier to monitor and manage your IT environment.

## Prerequisites

Before using the InfraSonar Appliance Manager, ensure you have the following prerequisites installed:

- Python _(inclusing pip)_
- Curl

You can install these prerequisites on Ubuntu or Debian-based systems using the following commands:
```
sudo apt update
sudo apt install python curl pip
```

Additionally, Docker Compose is required for the InfraSonar appliance to function properly. You can install Docker Compose using the following command:
```
sudo curl -sSL https://get.docker.com | bash
```

## Installation

To install the InfraSonar Appliance Manager, use the following command:
```
pip install infrasonar-appliance
```

## Usage

Once installed, simply start the tool using the following command:
```
appliance
```

The tool will handle the installation and management of your [InfraSonar appliance](https://docs.infrasonar.com/collectors/probes/appliance/), allowing you to focus on monitoring and managing your IT infrastructure.

## Additional Notes

- For more detailed instructions and troubleshooting guidance, refer to the official [InfraSonar documentation](https://docs.infrasonar.com).
- If you encounter any issues during installation or usage, feel free to [contact](https://infrasonar.com/contact) the InfraSonar support team for assistance.
