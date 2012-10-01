
import optparse

class Parser:

    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option('-b', '--batch-size', dest='batchsize', default=10, help='messages per batch')
        self.parser.add_option('-m', '--mailbox', dest='mailbox', default="INBOX", help='mailbox to query')
        self.parser.add_option('-c', '--config', dest='config', default=None, help='configuration file')
        self.parser.add_option('-s', '--setup', action="store_true", dest='setup', help='setup ~/.pickmailrc configuration file')
        self.parser.add_option('-w', '--wat', action="store_true", dest='password', help='save password in configuration file')
        self.options = None
        self.args = None

    def parse_cli(self, configuration):
        self.options, self.args = self.parser.parse_args()
        if self.options.config:
            configuration = pickmail.Config(config_file=self.options.config)
        if self.options.setup:
            configuration.setup_config(persist=True, store_pass=self.options.password)
        if self.options.batchsize:
            configuration.batchsize = self.options.batchsize
        if self.options.mailbox:
            configuration.mailbox = self.options.mailbox
        return configuration
