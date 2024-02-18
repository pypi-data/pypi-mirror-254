from application import AbstractApp

# Define module-level variables with version-related information
with open('version.dat', 'r') as _version:
    __version__ = _version.read()


# Function to retrieve the version
def version():
    """Returns the version of the module."""
    return __version__
