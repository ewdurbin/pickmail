
import imaplib
import email
from email.header import decode_header

def get_decoded_string(string_list):
    decoded = []
    for string in string_list:
        if string[1]:
            decoded.append(string[0].decode(string[1]))
        else:
            decoded.append(string[0])
    return " ".join(decoded)

class Connection:

    def __init__(self, config):
        if not config.password:
            config.setup_config()
        self.mailserver = imaplib.IMAP4_SSL(config.server, int(config.port))
        self.mailserver.login(config.username, config.password)
        self.mailserver.select(config.mailbox, readonly=True)
        self.data = None

    def get_message_list(self, count=10, offset=0, search_str="ALL"):
        result, data = self.mailserver.uid('search', None, search_str) 
        mail_list = data[0].split()
        start = -(count + offset + 1)
        end = -(offset + 1)
        if end == -1:
            return mail_list[start:]
        return mail_list[start:end]

    def get_message_headers(self, message_uid_list):
        query_str = ','.join(message_uid_list)
        result, data = self.mailserver.uid('fetch', query_str, '(BODY[HEADER])') 
        return data

    def dict_of_messages(self, count=10, offset=0, search_str="ALL"):
        message_list = self.get_message_list(count, offset, search_str)
        rev_message_list = message_list[::-1] 
        data = self.get_message_headers(message_list)
        message_map = {}
        i = 0
        for msg in reversed(data):
            if msg != ')':
                email_msg = email.message_from_string(msg[1])
                from_str = get_decoded_string(decode_header(email_msg['From']))
                subj_str = get_decoded_string(decode_header(email_msg['Subject']))
                if subj_str == "":
                    subj_str = "(No Subject)"
                info = "%s:   %5s\n\t%s\n" % (i, from_str, subj_str) 
                message_map[i] = {'uid': rev_message_list[i], 'info': info}
                i = i + 1 
        return message_map
        
    def get_messages(self, count=10, offset=0):
        self.data = self.dict_of_messages(count=count, offset=offset)
        ret = ""
        for k, v in self.data.items():
            ret += v['info']
        return ret

    def fetch_message(self, uid):
        result, data = self.mailserver.uid('fetch', uid, '(RFC822)')
        return data[0][1]
