#!/usr/bin/env python3
import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))

for arg in sys.argv[1:]:
  print(arg)
  print(type(arg))
print(int(sys.argv[1]))