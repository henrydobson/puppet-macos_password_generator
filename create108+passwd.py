#!/usr/bin/env python
import hashlib
import binascii
import os, sys

password = sys.argv[0]
salt = os.urandom(32)
puppet_salt = binascii.hexlify(salt)
iterations = 25000

hex = hashlib.pbkdf2_hmac('sha512', password, salt, 25000, 128)
puppet_password_hash = binascii.hexlify(hex)

print "password:", puppet_password_hash
print "salt:", puppet_salt
print "iterations:", iterations
