# originating code: https://coderzcolumn.com/tutorials/python/imaplib-simple-guide-to-manage-mailboxes-using-python

import imaplib
import email
import time
import json

global _EMAILDIR_
_EMAILDIR_ = "INBOX"


start = time.time()
try:
    imap_ssl = imaplib.IMAP4_SSL(host="imap.gmail.com", port=imaplib.IMAP4_SSL_PORT)
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    imap_ssl = None

try:
    resp_code, response = imap_ssl.login("alawson@aqorn.com","ehawuknmsiozktwn")
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    resp_code, response = None, None

resp_code, directories = imap_ssl.list(pattern=_EMAILDIR_)
for directory in directories:
    directory_name = directory.decode().split('"')[-2]
    directory_name = '"' + directory_name + '"'
    if directory_name == '"[Gmail]"':
        continue
    try:
        resp_code, mail_count = imap_ssl.select(mailbox=directory_name, readonly=True)
        count = mail_count[0].decode()
    except Exception as e:
        resp_code, mail_count = None, None

imap_ssl.close()
print (count)