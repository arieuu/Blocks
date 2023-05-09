import os
import shutil

# Go through all images in the dir and see if the current component has one in there
# If so it will be copied over, if not nothing happens.

def copyimg(section, variation, path):
    imgs = os.listdir("blocks/img/")
    filename = section + str(variation)

    for name in imgs:
        if name.split(".")[0] == filename:

            # If destination already exists it will be replaced

            shutil.copy("blocks/img/" + name, path + "/img/")
            print("done")
        