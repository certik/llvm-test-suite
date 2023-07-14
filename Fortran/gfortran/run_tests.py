#!/usr/bin/env python

import glob
import os

files_all = glob.glob("regression/*.f90")
files = []
for f in files_all:
    try:
        s = open(f).read()
    except UnicodeDecodeError:
        continue
    if s.find(r"{ dg-options") != -1:
        files.append(f)
N = len(files)
print("Number of f90 tests:", N)
fail = 0
for n, f in enumerate(files):
    r = os.system(f"lfortran --no-warnings --show-ast --no-color {f} &> a.ast")
    ok = True
    if r != 0:
        ok = False
    if not ok: fail += 1
    print(f"{n} / {N}: {f}, {ok}")
    if n > 30: break
print(f"Passed {fail} / {N}")
print("Done")
