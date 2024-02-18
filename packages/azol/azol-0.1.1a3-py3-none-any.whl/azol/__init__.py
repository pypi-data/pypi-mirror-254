"""azol module, which imports all other modules"""
from pathlib import Path
from azol.constants import AZOL_HOME, PROVIDER_CACHE_DIR, PROVIDER_CACHE

# Create the azol home directory
Path(AZOL_HOME).mkdir(parents=True, exist_ok=True)

# Create the folder structure below
Path(PROVIDER_CACHE_DIR).mkdir(parents=True, exist_ok=True)
Path(PROVIDER_CACHE).touch(exist_ok=True)
