import svn.remote


class VCS:
    def __init__(self):
        pass

    @staticmethod
    def svn_checkout(url, data_dir):
        svn_client = svn.remote.RemoteClient(url)
        svn_client.checkout(data_dir)
        return svn_client.info()
