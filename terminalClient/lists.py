#!/bin/env python3
#
# lists: a terminal client implementation for the lists web app.
#
#   Rick Wightman, September, 2018
#
# Testing the lists api proves hard to manage and therefore overwhelming
# using individual scripts. Memories of the distant past reminded me that
# there is value in the old display-a-list and ask for the choice number might
# be a more cohesive and intelligible strategy. So here goes!
#
# -*- coding: utf-8 -*-
from utils import *
import getpass
import bcrypt
import subprocess
# A rough plan of comments

################################################################################
# Start session:
#   Ask to login (no is ok)
#   Collect login credentials
#       Login, display results
#   NextMenu
quit = False
while not quit:
    if yes_no( "Login? (Y/n)" ):
        username = input("username: ")
        hash = bcrypt.hashpw( getpass.getpass().encode(), bcrypt.gensalt() )
        print(username+' ; '+hash.decode())

    print('Onward!')

    loginArgs = '-i -H \"Content-Type: application/json\" -X POST -d '
    loginArgs = loginArgs + '\'{\"userEmail\" : \"%s\", \"userPassword\" : \"%s\"}\''
    loginArgs = loginArgs + ' -k -c cookie-jar https://lists.hopto.org:61340/signin'
    loginArgs = loginArgs%(username,hash.decode())
    #curl command, store and interpret json
    result = subprocess.call(['curl', loginArgs])
    print(result)
print('Done.')
