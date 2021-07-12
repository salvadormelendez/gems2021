#!/usr/bin/env python3

import os

#Download Steganography Script
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/steganography.py"
os.system(msg)

#Download Image for Steganography
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/image.png"
os.system(msg)

#Download Dumpster Diving Script
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/dumpster_diving.py"
os.system(msg)

#Download Profiles Directory
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/profiles.tar.gz"
os.system(msg)

#Un-tar Profiles Directory
msg = "tar -xvzf profiles.tar.gz -C /home/pi/"
os.system(msg)

#Delete Files (e.g. tar, setup.py)
msg = "rm profiles.tar.gz"
os.system(msg)
msg = "rm gems_setup.py"
os.system(msg)
