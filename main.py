from vcs import VCS
from filemanager import Filemanager

url = input("Please enter url: ")
data_dir = Filemanager.get_dir_path()
VCS.svn_checkout(url, data_dir)
Filemanager.remove_dir(data_dir + "/.svn")
Filemanager.zip_folder(data_dir)
Filemanager.remove_dir(data_dir)
