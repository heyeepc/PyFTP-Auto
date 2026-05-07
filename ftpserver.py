from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.log import LogFormatter
import logging

from pyftpdlib.servers import FTPServer

logging = logging.getLogger('pyftpdlib')
logging.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='pyftpdlib.log', encoding='utf-8')

ch.setFormatter(LogFormatter())
fh.setFormatter(LogFormatter())
logging.root.addHandler(ch)
logging.root.addHandler(fh)

authorizer = DummyAuthorizer()
authorizer.add_user('user', '12345', 'd:/', perm='elero_admin')
authorizer.add_anonymous('d:/')

handler = FTPHandler
handler.authorizer =authorizer

handler.passive_ports = range(2000,2333)

dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 300 * 1024
dtp_handler.write_limit = 300 * 1024
handler.dtp_handler = dtp_handler

server = FTPServer(('0.0.0.0', 80), handler)
server.max_cons =150
server.max_cons_per_ip = 15
server.serve_forever()
