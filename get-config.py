#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time, sys, os
sys.path.append('/usr/lib/python3.8/site-packages')
import pexpect

id = raw_input('id: ')
pw = raw_input('password: ')

f = open('list.txt', 'r')

for line in f:

    child = pexpect.spawn('telnet ' + line)

    child.expect('login:')
    child.sendline(id)

    child.expect('Password:')
    child.sendline(pw)

    child.expect('# ')
    child.sendline('get system session status')

    line = line.strip()
    fout = open( line + '_result.txt','w')
    child.logfile = fout

    child.expect('# ')
    child.sendline('exit\n')
    child.close()
    child.logfile.close()
f.close()
