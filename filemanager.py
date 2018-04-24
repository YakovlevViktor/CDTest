import datetime
import shutil
import time
import os
import stat

import constants


class Filemanager:

    def __init__(self):
        self.temp_dir = constants.ROOT_DIR
        self.arch_dir = constants.ARCH_DIR

    def get_dir_path(self):
        timestamp = time.time()
        dir_path = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M')
        path = "%s/%s" % (self.temp_dir, dir_path)
        return path

    def zip_folder(self, dir_name):
        target_arch = "%s/%s" % (self.arch_dir, dir_name[self.temp_dir.__len__():])
        shutil.make_archive(target_arch, 'zip', dir_name)

    def remove_dir(self, dir_name):

        def on_rm_error(self, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)

        shutil.rmtree(dir_name, onerror=on_rm_error)
