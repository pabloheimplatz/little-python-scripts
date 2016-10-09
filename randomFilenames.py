# #! /usr/local/bin/python3
# Find a new random name for all files in one folder.

import random, os, re

def randomFilename(folder):
    for filename in os.listdir(folder):
        #print('original = ' +filename)

        # no invisible files like ._HEI_43_7584.JPG only names like HEI_52_7688.JPG
        #if filename == re.compile(r'[^._](HEI)(.*)'):
        if 'hei' == filename[:3].lower():
            #print("true = " +filename)
            randomValue = random.randint(0, 1000)

            # build new filenames
            old_file_name = '%s/%s' % (folder, filename)
            new_file_name = '%s/r%s_%s' % (folder, randomValue, filename)
            print(old_file_name)
            print(new_file_name)

            # ATTENTION!
            os.rename(old_file_name, new_file_name)

randomFilename(('PATH'))
