# originating code: https://coderzcolumn.com/tutorials/python/imaplib-simple-guide-to-manage-mailboxes-using-python

import imaplib
import email
import json
import sys
import os
from email.header import decode_header

global _EMAILDIR_
_EMAILDIR_ = sys.argv[1]

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# try:
#     imap_ssl = imaplib.IMAP4_SSL(host="imap.gmail.com", port=imaplib.IMAP4_SSL_PORT)
# except Exception as e:
#     print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
#     imap_ssl = None

# try:
#     resp_code, response = imap_ssl.login("alawson@aqorn.com","ehawuknmsiozktwn")
# except Exception as e:
#     print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
#     resp_code, response = None, None

# resp_code, directories = imap_ssl.list(pattern=_EMAILDIR_)
# directory_name = '"' + _EMAILDIR_ + '"'

# try:
#     resp_code, mail_count = imap_ssl.select(mailbox=directory_name, readonly=True)
#     count = mail_count[0].decode()
# except Exception as e:
#     resp_code, mail_count = None, None

# resp_code, mail_count = imap_ssl.select(mailbox=_EMAILDIR_, readonly=True)
# resp_code, mail_ids = imap_ssl.search(None, "ALL")




# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL('imap.gmail.com')
# authenticate
imap.login("alawson@aqorn.com","ehawuknmsiozktwn")


status, messages = imap.select(_EMAILDIR_, readonly=True)
# number of top emails to fetch
N = 3
# total number of emails
messages = int(messages[0])

all_messages = []
all_messages.append(messages)
# for mail_id in mail_ids[0].decode().split():

for mail_id in range(messages, 0, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(mail_id), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding)
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    try:
                        # get the email body
                        msg_body = part.get_payload(decode=True).decode()
                    except:
                        pass
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                msg_body = msg.get_payload(decode=True).decode()
            content = mail_id,email.utils.parseaddr(msg.get("From"))[0],email.utils.parseaddr(msg.get("From"))[1],msg.get("To"),msg.get("Bcc"),msg.get("Date"),msg.get("Subject"),msg_body
            all_messages.append(content)

imap.close()

print (json.dumps(all_messages))