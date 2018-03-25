#!/usr/bin/env python3

import sys

if len(sys.argv) == 2 and sys.argv[1]:
    print("Hello " + sys.argv[1])
else:
    print("Useage: " + sys.argv[0] + " <name>")


