import json
import os

import constants
from utils.filemanager import Filemanager
from utils.postgres import Batch, Task, db
from utils.vcs import VCS

input_dir = constants.INPUT_DIR
processed_dir = constants.PROCESSED_FILES_DIR
fm = Filemanager()
vcs = VCS()

for file in os.listdir(input_dir):
    batch = Batch(file_in=file)
    file_path = "%s/%s" % (input_dir, file)
    jfile = json.load(open(file_path))
    data_dir = fm.get_dir_path()

    for url in jfile['url']:
        print(url)

        task = Task(url=url)
        batch.tasks.append(task)

        endpoint_path = vcs.svn_checkout(url, data_dir)
        if endpoint_path is not None:
            task.status = 'OK'
            fm.remove_dir(endpoint_path + "/.svn")
        else:
            task.status = 'Failed'
            batch.status = 'Failed'

    print(data_dir)
    batch.file_out = fm.zip_folder(data_dir)
    fm.remove_dir(data_dir)

    db.session.add(batch)
    db.session.commit()

    processed_file = "%s/%s" % (processed_dir, file)
    os.rename(file_path, processed_file)
