#!/usr/bin/env python3

import os

#Download Steganography Script
wget -O steganography.py https://github.com/salvadormelendez/gems2021.git

#Download Image for Steganography
wget -O image.png https://github.com/salvadormelendez/gems2021.git

#Download Dumpster Diving Script
wget -O dumpster_diving.py https://github.com/salvadormelendez/gems2021.git

#Download Profiles Directory
wget -O profiles.tar.gz https://github.com/salvadormelendez/gems2021.git

#Un-tar Profiles Directory
msg = "tar -xvzf profiles.tar.gz -C /home/pi/"
os.system(msg)

#Delete Files (e.g. tar, setup.py)
msg = "rm profiles.tar.gz"
os.system(msg)
msg = "rm gems_setup.py"
os.system(msg)
