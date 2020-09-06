#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time, sys, os
sys.path.append('/usr/lib/python3.8/site-packages')

import pexpect
import getpass

#id = raw_input('id: ')
#pw = getpass.getpass()

f = open('list.txt', 'r')
c = open('cmd.txt', 'r')

const = ["ID","PASS"]

for line in f:

    line = line.strip()
    begin = line + ' connect .. '
    sys.stdout.write(begin)

    child = pexpect.spawn('telnet ' + line)
    
    expect_list = [u'Username:',
                   u'login:']

    child.expect(expect_list)
    child.sendline(const[0])

    child.expect('Password:')
    child.sendline(const[1])

    str = line + ' #'
    child.expect(str)

    for word in c:
        word = word.split(",")
        child.sendline(word[1])
        fn = line + '_' + word[0] + '.txt'
        spath = os.path.join('./log',fn)
        fout = open( spath,'w')
        child.logfile = fout
        child.expect(str)
    c.close()

    child.expect(str)
    child.sendline('exit\n')
    child.close()
    child.logfile.close()
    print ' done'
f.close()
