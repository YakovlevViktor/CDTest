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
        path = "%s/%s" % (dir_path, self.root_dir)
        return path

    def zip_folder(self, dir_name):
        base_name = "%s%s" % (self.root_dir, dir_name)
        shutil.make_archive(base_name, 'zip', dir_name)

    def remove_dir(self, dir_name):
        target_dir = "%s/%s" % (self.root_dir, dir_name)

        def on_rm_error(self, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)

        shutil.rmtree(target_dir, onerror=on_rm_error)
