import glob
import os
import re
import subprocess
import sys


EXCLUDE_DIRS = ['.github', '.git', '__pycache__']
IMAGE_EXTENSIONS = ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'svg', 'webp']
TITLE_PATTERN = re.compile('#(.*)\n')


def build(inputdir, outputdir):

    subdirs = [f.path for f in os.scandir(inputdir) if f.is_dir()]
    content_dirs = [d for d in subdirs if d.split('/')[-1] not in EXCLUDE_DIRS]

    # clean out outputdir
    os.makedirs(outputdir, exist_ok=True)
    outfiles = glob.glob(os.path.join(outputdir, '*'))
    for f in outfiles:
        os.remove(f)

    for d in content_dirs:

        category = d.split('/')[-1]
        content_files = glob.glob(os.path.join(d, '*.md'))

        for infile in content_files:
            outfile = os.path.join(outputdir, infile.split('/')[-1])
            date = git_commit_date(infile)

            with open(infile, 'r') as i:
                # a valid note must have a markdown H1 as its first line
                title = i.readline()
                if title[0:2] != '# ':
                    print(f'Invalid note {infile}! Skipping...')
                else:
                    title = title[2:].rstrip()

                    if os.path.isfile(outfile):
                        outfile = outfile.split('.')
                        outfile = outfile[0] + '-2' + outfile[1]

                    with open(outfile, 'w') as o:

                        o.write(f'Title: {title}\n')
                        if date:
                            o.write(f'Date: {date}\n')
                        o.write(f'Category: {category}\n')

                        for line in i:
                            o.write(line)
    

def git_commit_date(filename):
    CMD = f'git log -1 --format=%ci {filename}'
    resp = subprocess.run(CMD, shell=True, capture_output=True, text=True)
    if resp.stdout:
        datestr, *_ = resp.stdout.split()
        return datestr


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
    


