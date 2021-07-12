#!/usr/bin/env python3

import os

#Download Steganography Script
wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/steganography.py

#Download Image for Steganography
wget https://github.com/salvadormelendez/gems2021/raw/main/image.png

#Download Dumpster Diving Script
wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/dumpster_diving.py

#Download Profiles Directory
wget https://github.com/salvadormelendez/gems2021/raw/main/profiles.tar.gz

#Un-tar Profiles Directory
msg = "tar -xvzf profiles.tar.gz -C /home/pi/"
os.system(msg)

#Delete Files (e.g. tar, setup.py)
msg = "rm profiles.tar.gz"
os.system(msg)
msg = "rm gems_setup.py"
os.system(msg)
