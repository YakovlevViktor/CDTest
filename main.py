from vcs import VCS
from filemanager import Filemanager

import testdata

url = testdata.url
fm = Filemanager()
vcs = VCS()

data_dir = fm.get_dir_path()
vcs.svn_checkout(url, data_dir)
fm.remove_dir(data_dir + "/.svn")
fm.zip_folder(data_dir)
fm.remove_dir(data_dir)
