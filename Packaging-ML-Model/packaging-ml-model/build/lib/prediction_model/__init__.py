import os 
from prediction_model.config import config
# Return the version of the package by reading the package defined in the VERSION file
with open(os.path.join(config.PACKAGE_ROOT,'VERSION')) as f :
    __version__ = f.read().strip()
