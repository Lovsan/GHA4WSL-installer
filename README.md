# Home Assistant WSL Installer

![PyQt6](https://img.shields.io/badge/PyQt6-6.0.0-blue) ![Python](https://img.shields.io/badge/Python-3.7%2B-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

The **Home Assistant WSL Installer** is a graphical tool built with **PyQt6** designed to simplify the process of setting up [Home Assistant](https://www.home-assistant.io/) on a **WSL (Ubuntu on Windows)** environment. It automates the creation of a Python virtual environment, installs necessary dependencies (like the `wheel` package), and finally installs Home Assistant—all while providing real-time logging and embedded documentation.

---

## Prerequisites

Before running the installer, ensure that:

1. **WSL (Ubuntu):** You have a working Ubuntu distribution set up under WSL. If you haven't installed WSL yet, follow the [official Microsoft WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install).
2. **Python 3 and pip:** These should be installed within your WSL environment. To install Python 3 and pip, run:
```bash
   sudo apt update
   sudo apt install python3 python3-pip
````
**Permissions:** You must have write permissions to the /srv/ directory. If needed, use sudo to grant proper permissions:
´´´bash
sudo mkdir -p /srv/homeassistant
sudo chown -R $USER:$USER /srv/homeassistant
```

## Key Features
-**Graphical Interface:** A user-friendly GUI built with **PyQt6.**
-**Automated Installation:**    
-**Virtual Environment:** Creates a Python virtual environment at */srv/homeassistant.*
-**Dependency Installation:** Automatically installs the wheel package and Home Assistant.
-**Installation Logs:* Real-time display of log messages during the installation process.
-**Documentation:** Provides an Instructions tab within the application and a menu option to view a detailed **README**.
