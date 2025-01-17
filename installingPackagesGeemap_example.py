
# Unix/macOS


# from https://packaging.python.org/en/latest/tutorials/installing-packages/

# Ensure you can run Python from the command line.
# Before you go any further, make sure you have Python and that the expected version is 
# available from your command line. You can check this by running:

python3 --version

# Ensure you can run pip from the command line.
# Additionally, you’ll need to make sure you have pip available. You can check this by running:

python3 -m ensurepip --default-pip

# If you’re on Linux and installed using your OS package manager, you may have to install pip separately:
# from https://packaging.python.org/en/latest/guides/installing-using-linux-tools/

# Debian/Ubuntu and derivatives

# Firstly, update and refresh repository lists by running this command:

sudo apt update

sudo apt install python3-venv python3-pip

# from https://packaging.python.org/en/latest/tutorials/installing-packages/
# Ensure pip, setuptools, and wheel are up to date
# While pip alone is sufficient to install from pre-built binary archives, up to date copies of the 
# setuptools and wheel projects are useful to ensure you can also install from source archives:

python3 -m pip install --upgrade pip setuptools wheel

# create a virtual environment.

python3 -m venv tutorial_env
source tutorial_env/bin/activate # it activates the environment
# This will create a new virtual environment in the tutorial_env subdirectory, and configure the current shell to use it as the default python environment.

# now you can install geemap package

pip install geemap[lidar] open3d


#### now an example of code showinf Lidar data: ####

# from https://pypi.org/project/gdown/
# in order to run code where you have to download files from external source
pip install gdown

# to upgrade
pip install --upgrade gdown

# code:

# from https://geemap.org/notebooks/101_lidar/

# !pip install geemap[lidar] open3d

import os
import geemap

# Download a sample LiDAR dataset from Google Drive. The zip file is 52.1 MB and the uncompressed LAS file is 109 MB.

url = (
    "https://drive.google.com/file/d/1H_X1190vL63BoFYa_cVBDxtIa8rG-Usb/view?usp=sharing"
)
filename = "madison.las"

if not os.path.exists(filename):
    geemap.download_file(url, "madison.zip", unzip=True)

# Read the LiDAR data
las = geemap.read_lidar(filename)

# The LAS header.
las.header

# The number of points.
las.header.point_count

# The list of features.
list(las.point_format.dimension_names)

# Inspect data.
las.X
las.Y
las.Z
las.intensity

# Visualize LiDAR data using the pyvista backend.
geemap.view_lidar(filename, cmap='terrain', backend='pyvista')

# Visualize LiDAR data using the ipygany backend.
geemap.view_lidar(filename, backend='ipygany', background='white')

# Visualize LiDAR data using the panel backend.
geemap.view_lidar(filename, cmap='terrain', backend='panel', background='white')

# Visualize LiDAR data using the open3d backend.
geemap.view_lidar(filename, backend='open3d')































