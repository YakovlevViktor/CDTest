import datetime
import os
import shutil
import stat
import time

from init import config


class Filemanager:

    def __init__(self):
        self.config = config
        self.temp_dir = "%s%s" % (self.config.WORK_DIR, 'temp')
        self.arch_dir = "%s%s" % (self.config.WORK_DIR, 'arch')

    def get_dir_path(self):
        timestamp = time.time()
        dir_path = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S')
        path = "%s/%s" % (self.temp_dir, dir_path)
        return path

    def zip_folder(self, dir_name):
        target_arch = "%s/%s" % (self.arch_dir, dir_name[self.temp_dir.__len__() + 1:])
        shutil.make_archive(target_arch, 'zip', dir_name)
        return target_arch

    def remove_dir(self, dir_name):
        def on_rm_error(self, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)

        shutil.rmtree(dir_name, onerror=on_rm_error)
