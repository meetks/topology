#!/usr/bin/python -tt 

import pexpect
import sys, os
import getpass
import re

def main(argv):
  ip = set()
  txt = argv[0] + " " + argv[1]
  string = "telnet " + txt
  usr = raw_input("user:")
  pwd = getpass.getpass()
  child = pexpect.spawn(string)
  child.expect("scape");
  child.sendline("\n")
  i = child.expect(["login", "#", "switch#"])
  if i == 0:
    child.sendline(usr)
    child.expect("assword")
    child.sendline(pwd)
  child.sendline("show cdp neighbors detail | no-more")

  
  newip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', child.before)
  for x in newip:
   if x not in ip:
    ip.add(x)
  print 'IP address in network:', ip
  print 'Connections'
  print '----------------------------------'
  conn = re.findall(r'Ethernet\d+\/\d+\/\d+', child.before)
  i = 1
  for x in conn:
     if i < len(conn):
       print conn[i-1], '<------------------------>',conn[i]
     i = i + 1


if __name__ == '__main__':
  if len(sys.argv) < 2 :
    print 'Usage: telnet.py IP PORT '
  else:
    main(sys.argv[1:])
