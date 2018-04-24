from vcs import VCS
from filemanager import Filemanager

import testdata

url = testdata.url
fm = Filemanager()
vcs = VCS()

data_dir = fm.get_dir_path()

for url_entity in url:
    print(url_entity)
    endpoint_path = vcs.svn_checkout(url_entity, data_dir)
    fm.remove_dir(endpoint_path + "/.svn")
print(data_dir)
fm.zip_folder(data_dir)
fm.remove_dir(data_dir)
