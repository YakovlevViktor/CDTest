import svn.remote

import testdata


class VCS:
    def __init__(self):
        self.user = testdata.usr
        self.password = testdata.psw

    def svn_checkout(self, url, data_dir):
        svn_client = svn.remote.RemoteClient(url, username=self.user, password=self.password)
        svn_client.checkout(data_dir)
        return svn_client.info()
