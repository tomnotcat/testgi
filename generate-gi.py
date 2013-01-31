#!/usr/bin/env python
import sys, os

name = "g-ir-scanner.py"
path = os.environ['Path']
scanner = ""

for it in path.split (';'):
    if os.path.exists (it + os.path.sep + name):
        scanner = it + os.path.sep + name
        break

srcs = '''../testgi.h ../testgi.c'''

os.system ("cd " + sys.argv[1] + " && python.exe \"" + scanner + "\" --add-include-path=. --warn-all --namespace=TestGI --symbol-prefix=testgi \
 --nsversion=1.0 --no-libtool --include=GObject-2.0 \
 --pkg-export=TestGI-1.0 --library=" + sys.argv[2] + " --output TestGI-1.0.gir " + srcs +
" && g-ir-compiler --includedir=. TestGI-1.0.gir -o TestGI-1.0.typelib")
