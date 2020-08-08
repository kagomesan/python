#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time, sys, os
sys.path.append('/usr/lib/python3.8/site-packages')

import pexpect
import getpass

id = raw_input('id: ')
pw = getpass.getpass()

f = open('list.txt', 'r')

for line in f:

    child = pexpect.spawn('telnet ' + line)
    
    expect_list = [u'Username:',
                   u'login:']

    child.expect(expect_list)
    child.sendline(id)

    child.expect('Password:')
    child.sendline(pw)

    child.expect('# ')
    child.sendline('get system session status')

    line = line.strip()
    fn = line + '_result.txt'
    spath = os.path.join('./log',fn)
    fout = open( spath,'w')
    child.logfile = fout

    child.expect('# ')
    child.sendline('exit\n')
    child.close()
    child.logfile.close()
    print line + ' done'
f.close()
