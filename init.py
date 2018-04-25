import sys


class Config():
    WORK_DIR = '.'
    DB_CONNECT_STR = ''
    VCS_USR = ''
    VCS_PSW = ''

    def __init__(self, work_dir, db_connect_string, vcs_login, vcs_psw):
        self.WORK_DIR = work_dir
        self.DB_CONNECT_STR = db_connect_string
        self.VCS_USR = vcs_login
        self.VCS_PSW = vcs_psw


if len(sys.argv) != 5:
    print("Usage: python %s %s" % (sys.argv[0], " work_dir db_connect_string vcs_login vcs_psw"))
else:
    config = Config(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
