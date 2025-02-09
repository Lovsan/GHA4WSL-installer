import sys
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QTabWidget, QTextEdit, QLabel, QMenuBar, QMenu, QAction, QTextEdit, QPushButton 
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class welcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to Google Home Assistant Installer for WSL")
        self.setGeometry(100, 100, 600, 400) # x, y, width, height
        self.layout = QVBoxLayout()
        image_label = QLabel()
        image_label.setPixmap(QPixmap("google-home-assistant.png"))
        self.layout.addWidget(image_label)
        self.layout.addWidget(QLabel("Welcome to Google Home Assistant Installer for WSL!"))
        self.layout.addwidget(QLabel("This tool will help you install Home Assistant on Windows Subsystem for Linux (WSL)."))    
        # Add a button to start the installation process.
        self.lauout.addWidget(QLabel("This tool is designed to work on windows 10 with WSL enabled."))
        self.layout.addWidget(QPushButton("Next", clicked=self.open_installer))
        self.setLayout(self.layout)
        self.show()
        

class InstallerTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Home Assistant Installer for WSL")
        self.setGeometry(100, 100, 600, 400)

        # Set up the menu bar with a Help menu and a "View README" action.
        menubar = self.menuBar()
        help_menu = menubar.addMenu("Help")
        readme_action = QAction("View README", self)
        readme_action.triggered.connect(self.open_readme)
        help_menu.addAction(readme_action)

        # Set up the tab widget.
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create the Installer tab.
        self.install_tab = QWidget()
        self.install_layout = QVBoxLayout()
        self.install_button = QPushButton("Install Home Assistant")
        self.install_button.clicked.connect(self.install_home_assistant)
        self.install_layout.addWidget(self.install_button)

        # Log output area (read-only)
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.install_layout.addWidget(self.log_output)
        self.install_tab.setLayout(self.install_layout)
        self.tabs.addTab(self.install_tab, "Installer")

        # Create the Instructions tab.
        self.instructions_tab = QWidget()
        self.instructions_layout = QVBoxLayout()
        instructions_text = (
            "Installation Instructions:\n\n"
            "1. Ensure WSL (Ubuntu) is installed on your Windows system.\n"
            "2. Python 3 and pip should be installed in your WSL environment.\n"
            "3. This tool will create a virtual environment at /srv/homeassistant, install 'wheel', and then Home Assistant.\n"
            "4. Follow the on-screen log messages for progress and troubleshooting.\n"
        )
        self.instructions_label = QLabel(instructions_text)
        self.instructions_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.instructions_layout.addWidget(self.instructions_label)
        self.instructions_tab.setLayout(self.instructions_layout)
        self.tabs.addTab(self.instructions_tab, "Instructions")

    def install_home_assistant(self):
        self.log_output.append("Starting installation process...\n")
        try:
            # Step 1: Create the virtual environment
            venv_cmd = ["python3", "-m", "venv", "/srv/homeassistant"]
            self.log_output.append("Creating virtual environment at /srv/homeassistant ...")
            subprocess.run(venv_cmd, check=True)
            self.log_output.append("Virtual environment created successfully.\n")
            
            # Step 2: Install the 'wheel' package using the pip inside the virtual environment.
            pip_path = "/srv/homeassistant/bin/pip"
            install_wheel_cmd = [pip_path, "install", "wheel"]
            self.log_output.append("Installing 'wheel' package ...")
            subprocess.run(install_wheel_cmd, check=True)
            self.log_output.append("'wheel' installed successfully.\n")
            
            # Step 3: Install Home Assistant.
            install_ha_cmd = [pip_path, "install", "homeassistant"]
            self.log_output.append("Installing Home Assistant ...")
            subprocess.run(install_ha_cmd, check=True)
            self.log_output.append("Home Assistant installed successfully!\n")
            
            # Optionally, you could add code here to run Home Assistant initially
            # so it creates its default configuration:
            # hass_cmd = ["/srv/homeassistant/bin/hass"]
            # subprocess.run(hass_cmd, check=True)

        except subprocess.CalledProcessError as e:
            self.log_output.append(f"An error occurred during installation: {e}\n")

    def open_readme(self):
        """Open and display the README.md content in a new window."""
        try:
            with open("README.md", "r") as f:
                readme_content = f.read()
        except Exception as e:
            readme_content = f"Error opening README.md: {e}"
        # Create a simple window to display the README
        readme_window = QWidget()
        readme_window.setWindowTitle("README.md")
        layout = QVBoxLayout()
        readme_text = QTextEdit()
        readme_text.setPlainText(readme_content)
        readme_text.setReadOnly(True)
        layout.addWidget(readme_text)
        readme_window.setLayout(layout)
        readme_window.resize(500, 400)
        readme_text.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded) # Add scrollbar to the text edit
        readme_window.show()
        # Keep a reference to prevent garbage collection.
        self.readme_window = readme_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstallerTool()
    window.show()
    sys.exit(app.exec())
