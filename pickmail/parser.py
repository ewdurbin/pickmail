
import optparse

class Parser:

    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option('-s', '--server', dest='server', default=None, help='imap server')
        self.parser.add_option('-p', '--port', dest='port', default=None, help='imap port')
        self.parser.add_option('-u', '--user', dest='user', default=None, help='imap username')
        self.parser.add_option('-m', '--mailbox', dest='mailbox', default="INBOX", help='mailbox to query')
        self.parser.add_option('-b', '--batch-size', dest='batchsize', default=10, help='messages per batch')
        self.parser.add_option('-c', '--config', dest='config', default=None, help='configuration file')
        self.parser.add_option('--setup', action="store_true", dest='setup', help='setup ~/.pickmailrc configuration file')
        self.parser.add_option('-w', '--wat', action="store_true", dest='password', help='save password in configuration file')
        self.options = None
        self.args = None

    def parse_cli(self, configuration):
        self.options, self.args = self.parser.parse_args()
        if self.options.config:
            configuration = pickmail.Config(config_file=self.options.config)
        if self.options.setup:
            configuration.setup_config(persist=True, store_pass=self.options.password)
        if self.options.server:
            configuration.server = self.options.server
        if self.options.port:
            configuration.port = self.options.port
        if self.options.user:
            configuration.username = self.options.user
        if self.options.batchsize:
            configuration.batchsize = self.options.batchsize
        if self.options.mailbox:
            configuration.mailbox = self.options.mailbox
        return configuration
