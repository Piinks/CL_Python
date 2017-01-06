#!/usr/bin/env python3

# Kate Archer - Project 3 - p3mod.py
# CSCI 3038 - June 16, 2016

"""This module is intended for use imported into p3rmb.py"""

def read_one_fasta_entry(fasta):
    """This generator function will, on each invocation, return a single entry
    from a fasta file."""

    id = fasta.readline().strip().split()[0][1:]; sequence = ''

    for line in fasta:
        if line.startswith('>'):
            yield id, sequence
            id = line.strip().split()[0][1:];sequence = ''
        else:
            sequence += line.strip()
    yield id, sequence
