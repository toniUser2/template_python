import os
import subprocess


# =====================================================================================================
# requirements content
# =====================================================================================================
requirements_text = \
""" # ---- GENERATED --------
# example requirement
numpy
pytest
# ---- USER --------
"""

# =====================================================================================================
# readme content
# =====================================================================================================
readme_text = \
"""
# Description

# Doku
| Used Library  | Link                                          |
| --------      | -------                                       |
| numpy         | https://numpy.org/devdocs/user/index.html     |

# Python setup

Create virtual envirement
- python -m venv myenv

install requirements
- 


# User Guide
### How to use
### Setup via terminal
```
python -m venv myenv
./venv/Scripts/Activate.ps1
pip install -r .\requirements.txt
```
"""

# =====================================================================================================
# MAIN 
# =====================================================================================================
# 1. Überprüfen, ob die venv bereits vorhanden ist oder nicht.
venv_path = "venv"
if not os.path.exists(venv_path):
    # Wenn die venv nicht vorhanden ist, erstellen Sie sie.
    subprocess.run(["python", "-m", "venv", venv_path])

# 2. Überprüfen, ob requirements.txt bereits vorhanden ist oder nicht.
requirements_path = "requirements.txt"
if not os.path.exists(requirements_path):
    # Wenn requirements.txt nicht vorhanden ist, erstellen Sie es und schreiben Sie den vordefinierten Text.
    with open(requirements_path, "w") as f:
        f.write(requirements_text)  # Hier können Sie Ihre erforderlichen Pakete hinzufügen.

# 3. Installieren Sie die Anforderungen mit pip.
subprocess.run([os.path.join(venv_path, "Scripts" if os.name == "nt" else "bin", "pip"), "install", "-r", requirements_path])


# Überprüfen, ob README.md bereits vorhanden ist oder nicht.
readme_path = "README.md "
if not os.path.exists(readme_path):
    # Wenn requirements.txt nicht vorhanden ist, erstellen Sie es und schreiben Sie den vordefinierten Text.
    with open(readme_path, "w") as f:
        f.write(readme_text)  # Hier können Sie Ihre erforderlichen Pakete hinzufügen.