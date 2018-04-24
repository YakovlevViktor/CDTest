import datetime
import shutil
import time
import os
import stat

import constants


class Filemanager:
    def __init__(self):
        pass

    @staticmethod
    def get_dir_path():
        timestamp = time.time()
        dir_path = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M')
        path = "%s/%s" % (dir_path, constants.ROOT_DIR)
        return path

    @staticmethod
    def __get_root_dir():
        return constants.ROOT_DIR

    @staticmethod
    def zip_folder(dir_name):
        base_name = "%s%s" % (constants.ROOT_DIR, dir_name)
        base_dir = "%s/%s" % (dir_name, 'archives')

        shutil.make_archive(base_name, 'zip', dir_name)



    def remove_dir(dir_name):
        target_dir = "%s/%s" % (constants.ROOT_DIR, dir_name)

        def on_rm_error(self, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)

        shutil.rmtree(target_dir, onerror=on_rm_error)
