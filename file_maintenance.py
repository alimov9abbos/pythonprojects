# This python script is a script that Abbos Alimov wrote on 5/14/2020 to clean-up his messy
# Downloads folder that never gets organized. The script will move every file that is more
# than a week old to a folder for deletion/ relocation. This maintenance program only
# works on Windows operating systems.

import os
import shutil
import getpass
import stat
import time
from datetime import date
import datetime
from datetime import timedelta

# Warm Introduction :)
import datetime as datetime

print("This script is meant for all users who aren't hygienic about their Downloads folder on their Windows OS")
print('This script will create a folder on your desktop labeled as "ORGANIZEME" \n '
      'The script will then move files older than a week into this folder.')

x = input("Welcome to Abbos' Maintenance Script. If you wish to run the script please hit enter!")


# Desktop User path
org_path = os.environ['USERPROFILE'] + '\Desktop\ORGANIZEME'
# Downloads Path
downloads_path = os.environ['USERPROFILE'] + '\Downloads'

#Today's date
today = date.today()



#if the folder does not exist, make it.
if not os.path.exists(org_path):
    os.makedirs(org_path)

# Lets iterate through the downloads path
for filename in os.listdir(downloads_path):

        delta = 0
        #obtain the last modified date as a datetime object
        modtime = os.path.getmtime(os.path.join(downloads_path, filename))
        modtime = datetime.datetime.fromtimestamp(modtime)
        modtime = modtime.date()

        delta = (today-modtime).days

        #now both are date objects and we can get the difference



        # find the difference
        #delta = (today - last_m_date).days


        #if the file is a week old or older without mods, move it
        if (delta >= 7):
            shutil.move(os.path.join(downloads_path, filename),org_path)



print("Complete! Enjoy cleaning up that folder. :)")


