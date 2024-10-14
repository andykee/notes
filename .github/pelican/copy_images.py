import glob
import os
import re
import shutil
import subprocess
import sys


EXCLUDE_DIRS = ['.github', '.git', '__pycache__']
IMAGE_EXTENSIONS = ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'svg', 'webp']

def copy_images(inputdir, outputdir):

    print(inputdir, outputdir)

    subdirs = [f.path for f in os.scandir(inputdir) if f.is_dir()]
    content_dirs = [d for d in subdirs if d.split('/')[-1] not in EXCLUDE_DIRS]

    for d in content_dirs:

        # copy images to outputdir
        for e in IMAGE_EXTENSIONS:
            GLOB_STR = os.path.join(d, f'*.{e}')
            for image in glob.glob(GLOB_STR):
                shutil.copy(image, outputdir)


if __name__ == '__main__':
    copy_images(sys.argv[1], sys.argv[2])
