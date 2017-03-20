#!/usr/bin/env python3
import os.path
import subprocess
import sys
import urllib.parse

def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, encoding="utf-8")

path = sys.argv[1]
ref = run(["git", "rev-parse", "HEAD"]).stdout.strip()
root = run(["git", "rev-parse", "--show-toplevel"]).stdout.strip()
relpath = os.path.relpath(path, root)
ref, relpath = map(urllib.parse.quote, [ref, relpath])
print(f"https://nbviewer.jupyter.org/github/cesarkawakami/jupyter-notebooks/blob/{ref}/{relpath}")
