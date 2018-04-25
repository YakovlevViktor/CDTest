import svn.exception
import svn.remote

from init import config


class VCS:
    def __init__(self):
        self.config = config
        self.user = self.config.VCS_USR
        self.password = self.config.VCS_PSW

    def svn_checkout(self, url, data_dir):
        svn_client = svn.remote.RemoteClient(url, username=self.user, password=self.password)
        # Check if we could checkout repo
        try:
            enty_path = data_dir + svn_client.info().get('relative_url')[1:]
            svn_client.checkout(enty_path)
        except svn.exception.SvnException:
            return None
        else:
            return enty_path
