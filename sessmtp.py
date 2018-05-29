#! /usr/bin/env python3

import sys
import hmac
import hashlib
import base64

def smtp_password(aws_secret_key):
    '''
    Generate an SMTP password from an AWS secret key.
    '''
    key = aws_secret_key.encode('utf-8')
    message = "SendRawEmail".encode('utf-8')
    version = bytes(2)

    signature = hmac.new(
        key,
        msg=message,
        digestmod=hashlib.sha256
    ).digest()

    return base64.b64encode(version + signature).decode('utf-8')

if __name__ == '__main__':
    print(smtp_password(sys.argv[1]))
