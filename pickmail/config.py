
import os.path
import getpass
import ConfigParser

class Config:

    def _set_defaults(self):
        self.server = None
        self.port = None
        self.username = None
        self.password = None
        self.mailbox = "INBOX"

    def _build_config(self):
        config = ConfigParser.SafeConfigParser()
        config.add_section('pickmail')
        config.set('pickmail', 'server', '')
        config.set('pickmail', 'port', '')
        config.set('pickmail', 'mailbox', '')
        config.set('pickmail', 'username', '')
        config.set('pickmail', 'password', '')
        return config

    def _read_config(self, config_file):
        if os.path.isfile(config_file):
            self.config.read(config_file)
            self.server = self.config.get('pickmail', 'server')
            self.port = self.config.get('pickmail', 'port')
            self.mailbox = self.config.get('pickmail', 'mailbox')
            self.username = self.config.get('pickmail', 'username')
            self.password = self.config.get('pickmail', 'password')

    def __init__(self, config_file=os.path.expanduser('~/.pickmailrc')):
        self.config_file = config_file
        self._set_defaults()
        self.config = self._build_config()
        self._read_config(self.config_file)

    def setup_config(self, persist=False):
       if not self.server:
           prompt = "IMAP Server hostname?:\n"
           self.server = str(raw_input(prompt))
       if not self.port:
           prompt = "IMAP Server port?:\n"
           self.port = str(raw_input(prompt))
       if not self.mailbox:
           prompt = "IMAP Mailbox name?:\n"
           self.mailbox = str(raw_input(prompt))
       if not self.username:
           prompt = "IMAP Username for %s:%s ?:\n" % (self.server, self.port)
           self.username = str(raw_input(prompt))
       if not self.password:
           prompt = "IMAP Password for %s ?:\n" % (self.username)
           self.password = getpass.getpass(prompt)
       if persist:
           prompt = "Store IMAP Password? (yes/no)\n"
           persist = str(raw_input(prompt)).lower().strip()
           if persist == "yes":
               self.write_config(store_pass=True)
           else:
               self.write_config()

    def write_config(self, store_pass=False):
        self.config.set('pickmail', 'server', self.server)
        self.config.set('pickmail', 'port', self.port)
        self.config.set('pickmail', 'mailbox', self.mailbox)
        self.config.set('pickmail', 'username', self.username)
        self.config.set('pickmail', 'password', self.password)
        if not store_pass:
            self.config.remove_option('pickmail', 'password')
        with open(self.config_file, 'wb') as file:
            self.config.write(file)
