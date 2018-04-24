import datetime
import shutil
import time
import os
import stat

import constants


class Filemanager:

    def __init__(self):
        self.root_dir = constants.ROOT_DIR

    def get_dir_path(self):
        timestamp = time.time()
        dir_path = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M')
        path = "%s/%s" % (self.root_dir, dir_path)
        return path

    def zip_folder(self, dir_name):
        base_name = "%s%s" % (self.root_dir, dir_name)
        print(dir_name, base_name)
        shutil.make_archive(dir_name, 'zip')

    def remove_dir(self, dir_name):

        def on_rm_error(self, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)

        shutil.rmtree(dir_name, onerror=on_rm_error)
