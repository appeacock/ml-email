# originating code: https://coderzcolumn.com/tutorials/python/imaplib-simple-guide-to-manage-mailboxes-using-python

import imaplib
import email
import time
import json
import sys

global _EMAILDIR_
_EMAILDIR_ = sys.argv[1]


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

resp_code, mail_count = imap_ssl.select(mailbox=_EMAILDIR_, readonly=True)
resp_code, mail_ids = imap_ssl.search(None, "ALL")

messages = []
messages.append(count)
for mail_id in mail_ids[0].decode().split():
    content = ''
    resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)') ## Fetch mail data.
    message = email.message_from_bytes(mail_data[0][1])
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
    content = mail_id,message.get("From"),message.get("To"),message.get("Bcc"),message.get("Date"),message.get("Subject"),body.decode('utf-8')
    messages.append(content)

imap_ssl.close()
print (json.dumps(messages))