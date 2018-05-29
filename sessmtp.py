#! /usr/bin/env python3

import argparse
import hmac
import hashlib
import base64

def smtp_password(aws_secret_key):
    '''
    Generate an SMTP password from an AWS secret key.
    '''
    key = aws_secret_key.encode('utf-8')
    message = "SendRawEmail".encode('utf-8')
    version = b'\x02'

    signature = hmac.new(
        key,
        msg=message,
        digestmod=hashlib.sha256
    ).digest()

    return base64.b64encode(version + signature).decode('utf-8')

def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert an AWS Secret Key to an SMTP password for use'
                    ' with SES'
        )
    parser.add_argument(
        'AWS_SECRET_KEY',
        help='the key to convert into an SMTP password')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(smtp_password(args.AWS_SECRET_KEY))
