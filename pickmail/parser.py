
import optparse

class Parser:

    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option('-b', '--batch-size', dest='batchsize', default=10, help='messages per batch')
        self.parser.add_option('-m', '--mailbox', dest='mailbox', default="INBOX", help='mailbox to query')
        self.parser.add_option('-c', '--config', dest='config', default=None, help='configuration file')
        self.parser.add_option('-s', '--setup', action="store_true", dest='setup', help='setup configuration')
        self.parser.add_option('-p', '--persist', action="store_true", dest='persist', help='persist configuration to rcfile')
        self.parser.add_option('-w', '--wat', action="store_true", dest='password', help='save password in configuration file')
        self.options = None
        self.args = None

    def parse_cli(self):
        self.options, self.args = self.parser.parse_args()
