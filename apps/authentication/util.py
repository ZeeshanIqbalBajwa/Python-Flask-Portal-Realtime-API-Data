# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import hashlib
import binascii
import requests
import json


# Inspiration -> https://www.vitoshacademy.com/hashing-passwords-in-python/

# req_ip_token='10.60.90.40'
#req_ip_token='135.249.149.52'
#NSP_IP = '135.238.200.236'
# NSP_IP = '10.198.118.150'
NSP_IP = '147.75.102.178'

def hash_pass(password):
    """Hash a password for storing."""

    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash)  # return bytes


def verify_pass(provided_password, stored_password):
    """Verify a stored password against one provided by user"""

    stored_password = stored_password.decode('ascii')
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
