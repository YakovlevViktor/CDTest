import json
import os

import constants
from filemanager import Filemanager
from vcs import VCS

input_dir = constants.INPUT_DIR
processed_dir = constants.PROCESSED_FILES_DIR
fm = Filemanager()
vcs = VCS()

for file in os.listdir(input_dir):
    file_path = "%s/%s" % (input_dir, file)
    jfile = json.load(open(file_path))
    data_dir = fm.get_dir_path()

    for url in jfile['url']:
        print(url)
        endpoint_path = vcs.svn_checkout(url, data_dir)
        if endpoint_path is not None:
            fm.remove_dir(endpoint_path + "/.svn")

    print(data_dir)
    fm.zip_folder(data_dir)
    fm.remove_dir(data_dir)

    processed_file = "%s/%s" % (processed_dir, file)
    os.rename(file_path, processed_file)
