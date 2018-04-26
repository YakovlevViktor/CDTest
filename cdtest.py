import json
import os

from init import config
from utils.filemanager import Filemanager
from utils.postgres import Batch, Task, db
from utils.vcs import VCS

input_dir = "%s%s" % (config.WORK_DIR, 'input')
processed_dir = "%s%s" % (config.WORK_DIR, 'processed')
fm = Filemanager()
vcs = VCS()

# process each file in input dir
for file in os.listdir(input_dir):
    # new bd record
    batch = Batch(file_in=file)
    file_path = "%s/%s" % (input_dir, file)
    jfile = json.load(open(file_path))
    data_dir = fm.get_dir_path()

    # process each found url
    for url in jfile['url']:
        task = Task(url=url)
        #link task to the corresponding batch
        batch.tasks.append(task)

        endpoint_path = vcs.svn_checkout(url, data_dir)
        if endpoint_path is not None:
            task.status = 'OK'
            fm.remove_dir(endpoint_path + "/.svn")
        # smth went wrong during checkout
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
