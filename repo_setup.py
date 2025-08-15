import os
import subprocess
from pathlib import Path

dirs = [
    'artifacts',
    'config',
    'notebooks',
    'src',
    'static',
    'templates'
]

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Create __init__.py in package-like dirs
package_dirs = ['artifacts', 'config', 'src']
for d in package_dirs:
    Path(f"{d}/__init__.py").touch()

# Create .gitignore
Path('.gitignore').touch()

# Initialize git repo if not already present
if not Path('.git').exists():
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Repo initialized with basic structure"])
