"""doc"""

import psutil

for proc in psutil.process_iter():
    if len(proc.cmdline()) == 2:
        print(proc.cmdline()[1])

print(__name__)
print(__file__)
print(__cached__)
print(__package__)
print(__loader__)

print(__loader__.get_filename())
