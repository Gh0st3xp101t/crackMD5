#/usr/bin/python
#Script to crack hash MD5
import hashlib

password = raw_input('[*]Enter your md5 hash[*]')
passwordlist = raw_input('[*]Enter your list[*]')

passwordlist_read = open(passwordlist, 'r')

for line in passwordlist_read :
    line = line.strip()
    if hashlib.md5(line).hexdigest() == password :
        print '[!]hash cracked :[!]',line

    else :
        print '[:(]hash not cracked[:(]'
