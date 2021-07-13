#!/usr/bin/env python3

import os

users = ['gbecker', 'apalmer', 'spaterson', 'rchesterton', 'ikendal', 'vthornton', 'swarren', 'agibbs', 'jmathews', 'lderrick', 'dotis', 'eowen']
passwords = ['spiderman', 'batman', 'superman', 'ironman', 'darthvader', 'captainamerica', 'wonderwoman', 'blackwidow', 'scarletwitch', 'blackpanther', 'hawkeye', 'stormtrooper']

for i in range(len(users)):
    msg = "sudo useradd -m -p $(openssl passwd -1 " + passwords[i] + ") " + users[i]
    os.system(msg)
	
