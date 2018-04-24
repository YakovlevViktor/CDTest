import svn.remote

import testdata


class VCS:
    def __init__(self):
        self.user = testdata.usr
        self.password = testdata.psw

    def svn_checkout(self, url, data_dir):
        svn_client = svn.remote.RemoteClient(url, username=self.user, password=self.password)
        enty_path = data_dir + svn_client.info().get('relative_url')[1:]
        svn_client.checkout(enty_path)
        print(enty_path)
        return enty_path
