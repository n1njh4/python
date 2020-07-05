#!/usr/bin/python
# *-* encoding: utf-8 *-* 

import pexpect
import sys

child = pexpect.spawn('python /Users/n1njh4/Github/python/pexpect/question.py')
child.logfile = sys.stdout.buffer
child.expect('Are you human?')
child.sendline('y')
child.expect(pexpect.EOF)

