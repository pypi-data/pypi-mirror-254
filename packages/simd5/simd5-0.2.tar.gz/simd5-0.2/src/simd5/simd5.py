#!/usr/bin/env python3
#
# Python module to create MD5 files that contains the
#   MD5 hash of all the files in a subdirectory for digital deliveries.
# v 0.2
# 
# 31 Jan 2024
#
# Digitization Program Office,
# Office of the Chief Information Officer,
# Smithsonian Institution
# https://dpo.si.edu
#
# 
# Import modules
import hashlib
import os
import glob
from functools import partial

# from pathlib import Path
from time import localtime, strftime

# Parallel
import multiprocessing
from p_tqdm import p_map


def md5sum(filename, fileformat="m f"):
    """
    Get MD5 hash from a file.
    """
    # https://stackoverflow.com/a/7829658
    with open("{}".format(filename), mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    if fileformat == "m f":
        res = "{} {}".format(d.hexdigest(), os.path.basename(filename))
    elif fileformat == "f m":
        res = "{} {}".format(os.path.basename(filename), d.hexdigest())
    elif fileformat == "m,f":
        res = "{},{}".format(d.hexdigest(), os.path.basename(filename))
    elif fileformat == "f,m":
        res = "{},{}".format(os.path.basename(filename), d.hexdigest())
    return res



def md5_file(folder=None, fileformat="m f", workers=multiprocessing.cpu_count(), forced=False):
    for root, dirs, files_indir in os.walk(folder):
        for folder_check in dirs:
            if len(glob.glob("{}/{}/*.md5".format(root, folder_check))) > 0 and forced == False:
                print("\n   md5 file exists, skipping...\n")
                continue
            files = glob.glob("{}/{}/*".format(root, folder_check))
            if len(files) > 0:
                print("\n Running on folder {} using {} workers:".format(folder_check, workers))
                results = p_map(md5sum, files, fileformat, **{"num_cpus": int(workers)})
                with open("{}/{}/{}_{}.md5".format(root, folder_check, folder_check, strftime("%Y%m%d_%H%M%S", localtime())),
                        'w') as fp:
                    fp.write('\n'.join(results))
        if len(glob.glob("{}/*.md5".format(root))) > 0 and forced == False:
            print("\n   md5 file exists, skipping...")
            continue
        files = glob.glob("{}/*".format(root))
        if len(files) > 0:
            print("\n Running on folder {} using {} workers".format(root, workers))
            results = p_map(md5sum, files, **{"num_cpus": int(workers)})
            with open("{}/{}_{}.md5".format(root, os.path.basename(root), strftime("%Y%m%d_%H%M%S", localtime())), 'w') as fp:
                fp.write('\n'.join(results))


