#!/usr/bin/python3
# Mark Nesbitt
# 20170826
#
import sys
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: scriptname authfile")
        sys.exit()
    filename = sys.argv[1]
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        match = re.search(r'(\S\S\S \d\d \d\d:\d\d:\d\d) EARNEST sshd\[\d\d\d\d\d\]: Invalid user (\S+) from (\S+)',line) 
        if match:
            print(match.group(2), match.group(1), match.group(3))

if __name__ == '__main__':
    main()
