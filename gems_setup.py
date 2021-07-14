#!/usr/bin/env python3

import os

#Download Challenge
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/challenge.pdf"
os.system(msg)

#Download Shadow
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/shadow"
os.system(msg)

#Download Wordlist
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/cracking_wordlist.txt"
os.system(msg)

#Download Survey
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/survey.txt"
os.system(msg)

#Download Email Script
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/send_email.py"
os.system(msg)

#Download Steganography Script
msg = "wget https://raw.githubusercontent.com/salvadormelendez/gems2021/main/steganography.py"
os.system(msg)

#Download Images for Steganography
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/image.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_108.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_170.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_204.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_286.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_311.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_318.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_480.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_591.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_610.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_683.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_712.png"
os.system(msg)
msg = "wget https://github.com/salvadormelendez/gems2021/raw/main/new_image_717.png"
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
msg = "clear"
os.system(msg)
msg = "echo You are all set!"
os.system(msg)
