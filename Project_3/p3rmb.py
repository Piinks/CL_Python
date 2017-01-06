#!/usr/bin/env python3

import sys

import p3mod

f = open(sys.argv[1])
for (pegid,protseq) in p3mod.read_one_fasta_entry(f):
    print(pegid,protseq)

f.close()
