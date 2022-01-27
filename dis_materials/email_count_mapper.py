#!/usr/bin/env python3

import sys

for line in sys.stdin: # read input from STDIN
  line = line.strip() # remove leading and trailing whitespace
  if line.find("From:") == 0 and line.find("@") != -1:
            end_index = -1
            email_domain = line[line.find("@")+1:end_index]
            for i,char in enumerate(email_domain):
                if char != '.' or char != '-' or not char.isnumeric() or not char.isalpha():
                    email_domain = email_domain[0:i]
    if len(email_domain) == 0:
      email_domain == "empty"
    print ('%s\t%s' % (email_domain, 1)) # print output to STDOUT tab delimited
